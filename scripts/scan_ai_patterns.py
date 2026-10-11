# -*- coding: utf-8 -*-
"""Advisory scanner for a small set of Chinese readability patterns.

Protection covers common syntactic spans, not a full Markdown/TeX parser.
Findings do not establish AI origin, factual support, or mandatory edits.
"""

import argparse
from bisect import bisect_right
import json
import re
import sys


LIMITATIONS = [
    "Only a small set of Chinese readability patterns is scanned; every finding is advisory.",
    "Protection covers common syntactic spans, not a full Markdown/TeX parser: "
    "paired quotes, matching backtick runs, backtick/tilde fences, and paired $/$$ math. "
    "Unclosed fences protect to EOF; unclosed quotes, inline code, and math do not.",
    "Citation recognition is syntactic and incomplete; it does not verify sources or factual support.",
    "Results cannot determine AI origin, certify prose correctness, or predict detector scores.",
]

# IDs identify fixed rule groups and are independent of match order.
RULES = (
    ("FAW-PROMO-001", re.compile("全面赋能|里程碑|颠覆性创新|无限可能|不可磨灭|开创性"),
     "Review promotional wording against the supplied evidence and section context."),
    ("FAW-ATTR-001", re.compile("大量研究表明|专家普遍认为|业内普遍认为|众所周知"),
     "Review broad attribution and supply a specific source when the claim requires one."),
    ("FAW-RHET-001", re.compile(r"[？?](?=[ \t]*(?:答案|其实|正是))|难道[^。.;；!?！？\r\n\x00]{1,80}[？?]"),
     "Review the rhetorical question in context; a direct statement may be clearer."),
)
SENTENCE_BOUNDARY = re.compile(r"[。.!?！？；;\r\n]")
CITATION = re.compile(
    r"[（(][^（）()。！？；\r\n\x00]*(?:19|20)\d{2}[a-z]?[^（）()。！？；\r\n\x00]*[）)]"
    r"|\[\d+(?:\s*[-–,，]\s*\d+)*\]"
)
QUOTE_PAIRS = {"“": "”", "‘": "’", "「": "」", "『": "』", '"': '"', "'": "'"}
SPAN_TOKEN = re.compile(r"`+|\$+|[“‘「『\"']")
FENCE_OPEN = re.compile(r" {0,3}(`{3,}|~{3,})([^\r\n]*)")


def _escaped(text, offset):
    """An odd number of preceding backslashes escapes a delimiter."""
    start = offset
    while start and text[start - 1] == "\\":
        start -= 1
    return (offset - start) % 2 == 1


def _word_apostrophe(text, offset):
    """Keep apostrophes inside ordinary ASCII words out of quote matching."""
    return (0 < offset < len(text) - 1
            and text[offset - 1].isascii() and text[offset - 1].isalnum()
            and text[offset + 1].isascii() and text[offset + 1].isalnum())


def _plural_possessive(text, offset):
    """Do not open a quote at a trailing ASCII s-apostrophe (authors').

    Apply only to openers: a quote around 'results' must still close.
    """
    return (offset > 0 and text[offset - 1] in 'sS'
            and (offset + 1 == len(text)
                 or not (text[offset + 1].isascii() and text[offset + 1].isalnum())))


def _protected_text(text):
    """Mask spans without deleting characters or changing line endings."""
    chars = list(text)

    def protect(start, end):
        for index in range(start, end):
            if chars[index] not in "\r\n":
                chars[index] = "\x00"

    fence = None
    offset = 0
    for line in text.splitlines(keepends=True):
        if fence is not None:
            protect(offset, offset + len(line))
            marker, width = fence
            if re.fullmatch(r" {0,3}" + re.escape(marker) + "{" + str(width) + r",}[ \t]*", line.rstrip("\r\n")):
                fence = None
        else:
            opener = FENCE_OPEN.fullmatch(line.rstrip("\r\n"))
            if opener and not (opener[1][0] == "`" and "`" in opener[2]):
                fence = (opener[1][0], len(opener[1]))
                protect(offset, offset + len(line))
        offset += len(line)

    # This fence-only search view stays fixed. Matched spans move position past
    # their end, so later searches cannot revisit text masked in chars.
    masked = "".join(chars)
    position = 0
    while True:
        token = SPAN_TOKEN.search(masked, position)
        if token is None:
            break
        delimiter = token[0]
        position = token.end()
        if _escaped(text, token.start()):
            continue
        if delimiter.startswith("$") and len(delimiter) > 2:
            continue
        if delimiter == "'" and (_word_apostrophe(text, token.start())
                                 or _plural_possessive(text, token.start())):
            continue  # Do not treat an ordinary apostrophe as an opening quote.
        closer = QUOTE_PAIRS.get(delimiter, delimiter)
        closing_pattern = re.escape(closer)
        if delimiter[0] in "`$":
            closing_pattern = "(?<!" + re.escape(delimiter[0]) + ")" + closing_pattern + "(?!" + re.escape(delimiter[0]) + ")"
        for closing in re.compile(closing_pattern).finditer(masked, position):
            start, end = closing.span()
            if (text.find("\x00", token.end(), start) != -1
                    or (delimiter not in QUOTE_PAIRS
                        and masked.find("\x00", token.end(), start) != -1)):
                break  # Keep literal NUL barriers; only quotes can cross fences.
            if closer in ("'", "’") and _word_apostrophe(text, start):
                continue
            if delimiter[0] != "`" and _escaped(text, start):
                continue
            if delimiter == "$" and any(masked.find(c, token.end(), start) != -1 for c in "\r\n"):
                break
            protect(token.start(), end)
            position = end
            break
    return "".join(chars)


def scan_text(text):
    """Return advisory findings with one-based Unicode, exclusive-end locations.

    The caller's string is never modified. Invalid or blank API input raises
    ValueError; the CLI reports input errors with exit code 2.
    """
    if not isinstance(text, str) or not text.lstrip("\ufeff").strip():
        raise ValueError("Input must be a nonblank text string.")
    masked = _protected_text(text)
    line_starts = [0] + [m.end() for m in re.finditer(r"\r\n|[\r\n]", text)]
    # Citation recognition stays syntactic. Periods inside a recognized span
    # (initials or et al.) do not end its attribution sentence.
    citation_periods = {offset for citation in CITATION.finditer(masked)
                        for offset in range(citation.start(), citation.end())
                        if masked[offset] == '.'}
    boundaries = [m.start() for m in SENTENCE_BOUNDARY.finditer(masked)
                  if m.start() not in citation_periods]

    def location(offset):
        line = bisect_right(line_starts, offset)
        return line, offset - line_starts[line - 1] + 1

    findings = []
    # Only the question-mark cue uses lookahead at the immediate answer opener;
    # no finding consumes text from a second sentence.
    for rule_id, pattern, message in RULES:
        for match in pattern.finditer(masked):
            if rule_id == "FAW-ATTR-001":
                index = bisect_right(boundaries, match.start())
                start = boundaries[index - 1] + 1 if index else 0
                end = boundaries[index] if index < len(boundaries) else len(masked)
                if CITATION.search(masked, start, end):
                    continue
            line, column = location(match.start())
            end_line, end_column = location(match.end())
            findings.append({
                "rule_id": rule_id, "severity": "review",
                "line": line, "column": column,
                "end_line": end_line, "end_column": end_column,
                "match": text[match.start():match.end()], "message": message,
            })
    return sorted(findings, key=lambda f: (f["line"], f["column"], f["rule_id"]))


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="backslashreplace")
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog="Exit codes: 0 = scan ran or help; 1 = explicit review gate matched; 2 = input error.",
    )
    inputs = parser.add_mutually_exclusive_group(required=True)
    inputs.add_argument("file", nargs="?", help="UTF-8 text file, with an optional BOM")
    inputs.add_argument("--text", help="Inline text to review")
    parser.add_argument("--format", choices=("text", "json"), default="text", help="Output format (default: text)")
    parser.add_argument("--fail-on", choices=("review",), help="Return exit code 1 only when review findings exist")
    args = parser.parse_args(argv)
    source = args.file if args.file is not None else "<inline text>"
    try:
        if args.file is not None:
            with open(args.file, encoding="utf-8-sig", newline="") as stream:
                text = stream.read()
        else:
            text = args.text
        findings = scan_text(text)
    except (OSError, UnicodeError, ValueError) as error:
        parser.error(str(error))

    payload = {"source": source, "findings": findings,
               "summary": {"review": len(findings)}, "limitations": LIMITATIONS}
    if args.format == "json":
        print(json.dumps(payload, ensure_ascii=True, indent=2))
    else:
        print(f"Source: {source}")
        for finding in findings:
            print(f"[review] {finding['rule_id']} "
                  f"{finding['line']}:{finding['column']}-"
                  f"{finding['end_line']}:{finding['end_column']} "
                  f"{finding['match']!r}: {finding['message']}")
        print(f"Review findings: {len(findings)} (advisory; human judgment required).")
        for limitation in LIMITATIONS:
            print(f"Limitation: {limitation}")
    return 1 if args.fail_on == "review" and findings else 0


if __name__ == "__main__":
    sys.exit(main())
