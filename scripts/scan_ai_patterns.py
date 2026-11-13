# -*- coding: utf-8 -*-
"""Advisory scanner for a small set of Chinese readability patterns.

Protection covers common syntactic spans, not a full Markdown/TeX parser.
Findings do not establish AI origin, factual support, or mandatory edits.
"""

import argparse
from bisect import bisect_right
import json
from pathlib import Path
import re
import sys
import unicodedata


LIMITATIONS = [
    "Only a small set of Chinese readability patterns is scanned; every finding is advisory.",
    "Protection covers common syntactic spans, not a full Markdown/TeX parser: "
    "paired quotes, matching backtick runs, backtick/tilde fences, and paired $/$$ math. "
    "Unclosed fences protect to EOF; unclosed quotes, inline code, and math do not.",
    "This scanner does not check attribution, citation attachment, or evidence.",
    "Results cannot determine AI origin, certify prose correctness, or predict detector scores.",
]

# IDs identify fixed rule groups and are independent of match order.
RULES = (
    ("FAW-PROMO-001", re.compile("全面赋能|里程碑|颠覆性创新|无限可能|不可磨灭|开创性"),
     "Review promotional wording against the supplied evidence and section context."),
    ("FAW-RHET-001", re.compile(r"[？?](?=[ \t]*(?:答案|其实|正是))|难道[^。.;；!?！？\r\n\x00]{1,80}[？?]"),
     "Review the rhetorical question in context; a direct statement may be clearer."),
)
SENTENCE_BOUNDARY = re.compile(r"[。.!?！？；;\r\n]")
LINE_ENDING = re.compile(r"\r\n|[\r\n]")
MARKDOWN_BLOCK = re.compile(
    r" {0,3}(?:>|<|#{1,6}(?:[ \t]|$)|(?:[-+*]|[0-9]{1,9}[.)])(?:[ \t]|$)"
    r"|`{3,}|~{3,}|\[[^\]\r\n]+\]:|(?:[-*_][ \t]*){3,}$|=+[ \t]*$)"
)
# Recognize the numeric token first; grouping and decimal marks are not
# sentence punctuation while they are part of that token.
PRICE_VALUE = r"\d+(?:[,，]\d{3}(?!\d))*(?:[.．]\d+)?"
PRICE_NUMBER = re.compile(rf"[+\-−]?{PRICE_VALUE}")
PRICE_RANGE = re.compile(rf"[^\S\r\n]*(?:[-−–—~～]|至|到)[^\S\r\n]*[+\-−]?{PRICE_VALUE}")
PRICE_QUALIFIER = re.compile(r"\([A-Za-z\u3400-\u9fff \t-]+\)|（[A-Za-z\u3400-\u9fff \t-]+）")
PROSE_DATE = re.compile(r"\d{4}(?:[-/]\d{1,2}){2}")
PROSE_YEAR = re.compile(r"\d{4}[^\S\r\n]*年")
HAN_RUN = re.compile(r"[\u3400-\u9fff]+")
MATH_TOKEN = re.compile(
    r"(?P<space>[^\S\r\n]+)|(?P<number>(?:\d+(?:[.．]\d+|[.．](?=\Z))?|[.．]\d+)(?:[eE][+\-−]?\d+)?)"
    r"|(?P<name>[A-Za-z\u0370-\u03ff]+|[\u3400-\u9fff]+)"
    r"|(?P<command>\\[A-Za-z]+|\\[,;! {}])"
    r"|(?P<op>[<>=!]=|[+\-−*/×÷·^_=<>≤≥≠＋－＊／＝＜＞])"
    r"|(?P<open>[(\[（{［])|(?P<close>[)\]）}］])|(?P<bar>\|)"
    r"|(?P<post>[!'′″]|\\%)|(?P<sep>[,，;；:：])"
)
MATH_GROUPS = dict(zip("([（{［|", ")]）}］|"))
MATH_DELIMITER_COMMANDS = {r"\{": ("open", "{"), r"\}": ("close", "}"), r"\lvert": ("open", "|"), r"\rvert": ("close", "|")}
MATH_OPERATOR_COMMANDS = {
    r"\cdot", r"\times", r"\div", r"\pm", r"\mp", r"\le", r"\leq",
    r"\ge", r"\geq", r"\ne", r"\neq", r"\approx", r"\equiv",
}
MATH_RELATIONS = set("=<>≤≥≠＝＜＞") | {
    "<=", ">=", "!=", "==", r"\le", r"\leq", r"\ge", r"\geq",
    r"\ne", r"\neq", r"\approx", r"\equiv",
}
MATH_TEXT_COMMANDS = {r"\text", r"\textrm", r"\textit", r"\textbf"}
MATH_TEXT_TOKEN = re.compile(r"\\(?:textrm|textit|textbf|text)(?![A-Za-z])")
MATH_SPACING = {r"\,", r"\;", r"\!", "\\ "}
MATH_SIGNS = "+-−＋－"
EN_PROSE = re.compile(r"[A-Za-z]{2,}[ \t]+(?:[A-Za-z]{2,}\b|[\u3400-\u9fff])")
QUOTE_PAIRS = {"“": "”", "‘": "’", "「": "」", "『": "』", '"': '"', "'": "'"}
INLINE_SPACE = re.compile(r"[^\S\r\n]*")
DOLLAR_OR_BARRIER = re.compile(r"\$+|\x00+|[\r\n]")
PRIME_RUN = re.compile(r"'+")
SPAN_TOKEN = re.compile(r"\x60+|\$+|[“”‘’「」『』\"']")
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
            and text[offset + 1].isascii() and text[offset + 1].isalpha())


def _plural_possessive(text, offset):
    """Do not open a quote at a trailing ASCII s-apostrophe (authors').

    Apply only to openers: a quote around 'results' must still close.
    """
    return (offset > 0 and text[offset - 1] in 'sS'
            and (offset + 1 == len(text)
                 or not (text[offset + 1].isascii() and text[offset + 1].isalnum())))


def _text_group_end(text, start, end):
    """End of one balanced TeX text argument, or None."""
    if start == end or text[start] != "{":
        return None
    depth = 0
    for pos in range(start, end):
        if text[pos] in "{}" and not _escaped(text, pos):
            depth += 1 if text[pos] == "{" else -1
            if depth == 0:
                return pos + 1
    return None


def _primed_call(text, start, end):
    """A multi-letter name can take a prime before a complete function call."""
    if start >= end or text[start] not in "(（":
        return False
    expected = []
    for pos in range(start, end):
        ch = text[pos]
        if ch == "'":
            return False
        if ch in "(（":
            expected.append(MATH_GROUPS[ch])
        elif ch in ")）":
            if not expected or expected.pop() != ch:
                return False
            if not expected:
                after = INLINE_SPACE.match(text, pos + 1, end).end()
                token = MATH_TOKEN.match(text, after, end)
                return after == end or bool(token and token.lastgroup == "op")
    return False


def _math_shape(text, start, end):
    """Return 0 for no shape, 1 for a complete shape, 2 for explicit outer math."""
    frames = []
    last = None
    prime_base = False
    previous = None
    evidence = word = saw_math = False
    segment_operator = segment_symbol = explicit = False
    pos = start
    while pos < end:
        token = MATH_TOKEN.match(text, pos, end)
        if token is None:
            return 0
        pos = token.end()
        kind, value = token.lastgroup, token[0]
        if kind == "space" or value in MATH_SPACING:
            continue
        if kind == "name":
            segment_symbol = True
        if kind == "command":
            if value in MATH_OPERATOR_COMMANDS:
                kind = "op"
            elif value in MATH_DELIMITER_COMMANDS:
                kind, value = MATH_DELIMITER_COMMANDS[value]
            elif value in (r"\left", r"\right"):
                after = MATH_TOKEN.match(text, INLINE_SPACE.match(text, pos, end).end(), end)
                if not after or (after.lastgroup not in ("open", "close", "bar")
                                 and after[0] not in MATH_DELIMITER_COMMANDS):
                    return 0
                continue
            elif value in MATH_TEXT_COMMANDS:
                group_end = _text_group_end(text, INLINE_SPACE.match(text, pos, end).end(), end)
                if group_end is None:
                    return 0
                pos = group_end
                kind = "group"
                evidence = True

        if kind == "bar":
            kind = "close" if frames and frames[-1][0] == "|" and last is not None else "open"
        if kind == "open":
            function = last == "command" or (last in ("name", "word") and value != "{")
            frames.append((MATH_GROUPS[value], evidence, word, function))
            last = None
            evidence = word = False
        elif kind == "close":
            if not frames or frames[-1][0] != value or last is None:
                return 0
            _, outer_evidence, outer_word, function = frames.pop()
            last = "group"
            evidence = evidence or outer_evidence or function
            word = word or outer_word
        elif kind == "sep":
            if last is None:
                return 0
            if not frames:
                # A bare prose-like word in a top-level segment cannot borrow
                # math evidence from a different segment.
                if word and not evidence:
                    return 0
                saw_math = saw_math or evidence
                explicit = explicit or (segment_operator and segment_symbol)
                segment_operator = segment_symbol = evidence = word = False
            last = None
        elif kind == "op":
            if last is None:
                if value not in MATH_SIGNS:
                    return 0
            else:
                evidence = True
                if not frames:
                    segment_operator = True
                    explicit = explicit or value in MATH_RELATIONS
                last = None
        elif kind == "post":
            if last is None:
                return 0
            if value == "'":
                call = last == "word" and _primed_call(text, pos, end)
                if (not (prime_base or call) or text[token.start() - 1].isspace()
                        or (pos < end and text[pos].isalnum())):
                    return 0
            last = "postfix"
            evidence = True
        else:
            if kind == "name" and len(value) > 1:
                kind = "word"
            if last in ("word", "name") and kind in ("word", "name") and "word" in (last, kind):
                return 0
            if last == "postfix" and kind == "word":
                return 0
            word = word or kind == "word"
            last = kind
        if kind != "post":
            prime_base = (kind in ("close", "command", "group")
                          or (kind == "number" and previous in ("^", "_"))
                          or (kind == "name" and len(value) == 1
                              and (value.isascii() or "\u0370" <= value <= "\u03ff")))
        previous = value
    if frames or last is None or (word and not evidence) or not (evidence or saw_math):
        return 0
    return 2 if explicit or (segment_operator and segment_symbol) else 1


def _price_body(text, start, end):
    """Distinguish price-like prose, dated prose and a short punctuated amount."""
    number = PRICE_NUMBER.match(text, start, end)
    if number is None:
        return "", False
    price_range = PRICE_RANGE.match(text, number.end(), end)
    number_end = price_range.end() if price_range else number.end()

    def separator(ch):
        return (ch.isspace() or (unicodedata.category(ch).startswith("P")
                                 and ch not in "\\_{}[]()（）-*/"))

    def after_separators(offset):
        while offset < end and separator(text[offset]):
            offset += 1
        return offset

    cursor = after_separators(number_end)
    qualifier = PRICE_QUALIFIER.match(text, cursor, end)
    if qualifier:
        cursor = after_separators(qualifier.end())
    if cursor == end:
        return ("short" if cursor > number_end else ""), False
    suffix = HAN_RUN.match(text, cursor, end)
    if (suffix and len(suffix[0]) <= 8 and not text[number_end:cursor].strip()
            and suffix.end() < end and after_separators(suffix.end()) == end):
        return "short", False

    date = False
    if cursor > number_end:
        numeric_date = PROSE_DATE.match(text, cursor, end)
        chinese_year = PROSE_YEAR.match(text, cursor, end)
        lead = numeric_date or PRICE_NUMBER.match(text, cursor, end)
        if lead:
            cursor = after_separators(lead.end())
            date = bool(numeric_date or chinese_year)
    han = HAN_RUN.match(text, cursor, end)
    prose = (cursor > number_end and (han or EN_PROSE.match(text, cursor, end))
             or han and han.end() < end and separator(text[han.end()]))
    return ("prose" if prose else ""), bool(prose and date)


def _pair_score(text, left, right):
    """Lexicographic evidence for one syntactically admissible dollar pair."""
    start = left + 1
    end = right + 1
    if (start == right or text[start].isspace() or text[right - 1].isspace()
            or (end < len(text) and text[end].isdigit())):
        return None
    price, dated = _price_body(text, start, right)
    if dated:
        return None
    shape = _math_shape(text, start, right)
    if price == "short":
        # A trailing mark can be price punctuation or a factorial. Keep a
        # noncompeting pair, but do not give it priority over complete math.
        return (0, 0, 1)
    if shape == 2:
        return (1, 0, 0)
    if shape == 1 and not price:
        return (0, 1, 0)
    if shape == 1:
        return (0, 0, 1)
    if price:
        return None
    if re.fullmatch(r"[A-Za-z\u0370-\u03ff]|\d+(?:[.．]\d+)?", text[start:right]):
        return (0, 1, 0)
    return (0, 0, 1)


def _certain_pairs(text, positions, disputed=None):
    """Return the adjacent edges present in every best non-overlapping plan."""
    size = len(positions)
    if size < 2:
        return
    empty = (0, 0, 0)

    def add(a, b):
        return tuple(x + y for x, y in zip(a, b))

    scores = [_pair_score(text, a, b) for a, b in zip(positions, positions[1:])]
    left = [empty] * (size + 1)
    right = [empty] * (size + 1)
    for i, score in enumerate(scores):
        left[i + 2] = max(left[i + 1], add(left[i], score)) if score else left[i + 1]
    for i in range(size - 2, -1, -1):
        score = scores[i]
        right[i] = max(right[i + 1], add(score, right[i + 2])) if score else right[i + 1]
    optimum = right[0]
    possible = [bool(score and add(add(left[i], score), right[i + 2]) == optimum)
                for i, score in enumerate(scores)]
    for i, can_pair in enumerate(possible):
        if can_pair:
            span = positions[i], positions[i + 1] + 1
            if (i == 0 or not possible[i - 1]) and add(left[i], right[i + 1]) != optimum:
                yield span
            elif disputed is not None:
                disputed.append(span)


def _dollar_groups(text, view):
    """Yield each run of single dollars between complete barriers."""
    group = []
    for mark in DOLLAR_OR_BARRIER.finditer(view):
        start = mark.start()
        if mark[0].startswith("$") and _escaped(text, start):
            continue
        if mark[0] == "$":
            group.append(start)
        elif group:
            yield group
            group = []
    if group:
        yield group


def _dollar_pairs(text, opaque, diagnostics):
    """Only a supported formula, certain across competing plans, is opaque."""
    pairs = {}
    for group in _dollar_groups(text, opaque):
        disputed = []
        for start, end in _certain_pairs(text, group, disputed):
            score = _pair_score(text, start, end - 1)
            if score != (0, 0, 1):
                pairs[start] = end
                continue
            # An explicit formula lead can resolve a weak but complete
            # math shape or an otherwise untyped single Han identifier.
            prefix = text[max(0, start - 12):start]
            body = text[start + 1:end - 1]
            introduced = re.search(r"(?:算式|公式)[：: ]*$", prefix)
            labelled_atom = re.fullmatch(r"(?:\d+(?:[.．]\d+)?)?(?:[\u3400-\u9fff]{1,8}|\([\u3400-\u9fff]{1,8}\))", body)
            if introduced and (_math_shape(text, start + 1, end - 1) or labelled_atom):
                pairs[start] = end
            else:
                disputed.append((start, end))
        diagnostics.extend(("dollar", start, end) for start, end in disputed)
    return pairs


def _math_inline_literals(text):
    """Only complete math candidates can own apostrophes or TeX text."""
    if "'" not in text and not MATH_TEXT_TOKEN.search(text):
        return []
    literals = []
    for group in _dollar_groups(text, text):
        for left, right in zip(group, group[1:]):
            begin = left + 1
            if ("'" not in text[begin:right] and not MATH_TEXT_TOKEN.search(text, begin, right)):
                continue
            if not _pair_score(text, left, right) or not _math_shape(text, begin, right):
                continue
            # The shape check has established that apostrophes outside TeX
            # text groups are conventional postfix primes.
            cursor = begin
            for command in MATH_TEXT_TOKEN.finditer(text, begin, right):
                if command.start() < cursor or _escaped(text, command.start()):
                    continue
                start = INLINE_SPACE.match(text, command.end(), right).end()
                end = _text_group_end(text, start, right)
                if end is not None:
                    literals.extend(m.span() for m in PRIME_RUN.finditer(text, cursor, command.start()))
                    literals.append((start, end))
                    cursor = end
            literals.extend(m.span() for m in PRIME_RUN.finditer(text, cursor, right))
    return literals


def _mask(chars, start, end):
    for i in range(start, end):
        if chars[i] not in "\r\n":
            chars[i] = "\x00"


def _fenced_text(text):
    """Mask structural fences; this view does not mask inline content."""
    chars = list(text)
    fence = None
    offset = 0
    for line in text.splitlines(keepends=True):
        if fence is not None:
            _mask(chars, offset, offset + len(line))
            marker, width = fence
            if re.fullmatch(r" {0,3}" + re.escape(marker) + "{" + str(width) + r",}[ \t]*", line.rstrip("\r\n")):
                fence = None
        else:
            opener = FENCE_OPEN.fullmatch(line.rstrip("\r\n"))
            if opener and not (opener[1][0] == "`" and "`" in opener[2]):
                fence = (opener[1][0], len(opener[1]))
                _mask(chars, offset, offset + len(line))
        offset += len(line)
    return "".join(chars)


# Closed-class English continuations distinguish a predicate after a closed
# quotation from a possessive dependent inside an open quotation.
EN_NON_NOMINAL = (
    r"(?:and|or|but|yet|then|however|is|are|was|were|am|has|have|had|do|does|did|"
    r"can|could|may|might|must|will|would|shall|should|ought|we|they|he|she|it|you|i)\b"
)
POSSESSION_GAP = r"[ \t]+|[ \t]*(?:\r\n|\r|\n)[ \t]*"
POSSESSIVE_NOMINAL = re.compile(rf"(?:{POSSESSION_GAP})(?!{EN_NON_NOMINAL})[A-Za-z0-9]", re.I)
POSSESSIVE_COORD = re.compile(
    rf"(?:{POSSESSION_GAP})(?:and|or)(?:{POSSESSION_GAP})"
    r"(?:[A-Za-z0-9-]+[ \t]+){0,5}[A-Za-z-]*s['’]"
    rf"(?=(?:{POSSESSION_GAP})(?!{EN_NON_NOMINAL})[A-Za-z0-9])", re.I,
)
BLANK_LINE = re.compile(r"(?:\r\n|\r(?!\n)|(?<!\r)\n)[ \t]*(?:\r\n|\r(?!\n)|(?<!\r)\n)")


def _atomic_delimiters(text, view, tokens, is_literal):
    """Map complete code/display openers to same-type closing token indices."""
    next_close = {}
    pairs = {}
    for i in range(len(tokens) - 1, -1, -1):
        token = tokens[i]
        marker = token[0]
        if marker[0] != "\x60" and marker != "$$":
            continue
        escaped = _escaped(text, token.start())
        if marker == "$$" and escaped:
            continue
        following = next_close.get(marker)
        if following is not None and not escaped and not is_literal(token.start()):
            if view.find("\x00", token.end(), tokens[following].start()) == -1:
                pairs[i] = following
        next_close[marker] = i
    return pairs


def _protected_text(text, masked, literals, diagnostics):
    """Parse typed spans once. A complete atomic or quoted child owns its delimiters."""
    chars = list(masked)
    starts = [start for start, _ in literals]
    tokens = list(SPAN_TOKEN.finditer(masked))

    def is_literal(offset):
        index = bisect_right(starts, offset) - 1
        return index >= 0 and offset < literals[index][1]

    atoms = _atomic_delimiters(text, masked, tokens, is_literal)

    def quote_opener(token):
        start, end = token.span()
        if token[0] not in QUOTE_PAIRS or _escaped(text, start) or is_literal(start):
            return False
        if token[0] == "'" and (_word_apostrophe(text, start) or _plural_possessive(text, start)):
            return False
        # A symmetric glyph attached to the preceding text and followed by
        # host punctuation/space is a closer, even after a block reset.
        if token[0] in ("'", '"') and start and masked[start - 1].isalnum():
            right = masked[end:end + 1]
            if not right or right.isspace() or SENTENCE_BOUNDARY.fullmatch(right) or right in ",，:：)]）]】":
                return False
        return True

    def quote_end(index, nested_pairs):
        opener = tokens[index]
        wanted = QUOTE_PAIRS[opener[0]]
        stop = text.find("\x00", opener.end())
        tentative = None
        symmetric_child = False
        i = index + 1
        while i < len(tokens):
            token = tokens[i]
            start, end = token.span()
            if stop != -1 and start >= stop:
                break
            if tentative is not None and BLANK_LINE.search(masked, tokens[tentative].end(), start):
                break
            if i in atoms:
                i = atoms[i] + 1
                continue
            i += 1
            if _escaped(text, start) or is_literal(start):
                continue
            if token[0] == wanted:
                if wanted in ("'", "’"):
                    if _word_apostrophe(text, start):
                        continue
                    if (tentative is not None and i - 1 in nested_pairs
                            and (masked[start - 1].isspace() or not masked[start - 1].isalnum())):
                        # A complete second pair is stronger evidence than
                        # the glyph or script of its first content character.
                        symmetric_child = True
                        i = nested_pairs[i - 1][0] + 1
                        continue
                    if _plural_possessive(text, start) and (
                        POSSESSIVE_NOMINAL.match(masked, end) or POSSESSIVE_COORD.match(masked, end)
                    ):
                        if tentative is None:
                            tentative = i - 1
                        continue
                if tentative is not None and symmetric_child:
                    return tentative, i - 1
                return i - 1, None
            if i - 1 in nested_pairs:
                i = nested_pairs[i - 1][0] + 1
        return None if tentative is None else (tentative, None)

    # Each potential child is to the right of its parent. Resolve those spans
    # first, so a parent can skip a complete child without recursive rescanning.
    quote_pairs = {}
    closing_marks = set()
    for i in range(len(tokens) - 1, -1, -1):
        token = tokens[i]
        if quote_opener(token) and QUOTE_PAIRS[token[0]] in closing_marks:
            end = quote_end(i, quote_pairs)
            if end is not None:
                quote_pairs[i] = end
        if not _escaped(text, token.start()) and not is_literal(token.start()):
            closing_marks.add(token[0])

    i = 0
    while i < len(tokens):
        token = tokens[i]
        closing = atoms.get(i)
        if closing is None:
            pair = quote_pairs.get(i)
            if pair:
                closing, disputed = pair
                if disputed is not None:
                    diagnostics.append(("quote", tokens[closing].end(), tokens[disputed].end()))
        if closing is None:
            i += 1
        else:
            _mask(chars, token.start(), tokens[closing].end())
            i = closing + 1
    return "".join(chars)


def _prose_regions(text, fenced, line_endings, starts, markdown):
    """Yield contiguous block-local source ranges before matching inline spans."""
    ends = [m.start() for m in line_endings] + [len(text)]
    region = None
    stop = 0
    for start, end in zip(starts, ends):
        raw = text[start:end]
        excluded = not fenced[start:end].strip("\x00 \t")
        standalone = markdown and bool(MARKDOWN_BLOCK.match(raw) or re.match(r" {0,3}\|", raw))
        if excluded or standalone:
            if region is not None:
                yield region, stop
                region = None
            if standalone and not excluded:
                yield start, end
        else:
            if region is None:
                region = start
            stop = end
    if region is not None:
        yield region, stop


def scan_text(text, *, input_format="text", diagnostics=None):
    """Return advisory findings with one-based Unicode, exclusive-end locations.

    The caller's string is never modified. Invalid or blank API input raises
    ValueError; the CLI reports input errors with exit code 2.
    """
    if not isinstance(text, str) or not text.lstrip("\ufeff").strip():
        raise ValueError("Input must be a nonblank text string.")
    if input_format not in ("text", "markdown"):
        raise ValueError("Input format must be text or markdown.")
    line_endings = list(LINE_ENDING.finditer(text))
    line_starts = [0] + [m.end() for m in line_endings]
    fenced = _fenced_text(text)
    uncertain = []
    chars = list(fenced)
    for start, end in _prose_regions(text, fenced, line_endings, line_starts, input_format == "markdown"):
        raw_block, block = text[start:end], fenced[start:end]
        bounds = []
        literals = _math_inline_literals(block) if "$" in block else []
        opaque = _protected_text(raw_block, block, literals, bounds)
        chars[start:end] = opaque
        if "$" in opaque:
            for left, right in _dollar_pairs(block, opaque, bounds).items():
                _mask(chars, start + left, start + right)
        uncertain.extend((kind, start + a, start + b) for kind, a, b in bounds)
    masked = "".join(chars)
    def location(offset):
        line = bisect_right(line_starts, offset)
        return line, offset - line_starts[line - 1] + 1

    if diagnostics is not None:
        for kind, a, b in sorted(set(uncertain), key=lambda x: (x[1], x[2], x[0])):
            line, column = location(a)
            end_line, end_column = location(b)
            diagnostics.append({"kind": kind, "line": line, "column": column,
                                "end_line": end_line, "end_column": end_column,
                                "message": "保护边界待核：争议文字保留可见，修改前须确认。"})

    findings = []
    # Only the question-mark cue uses lookahead at the immediate answer opener;
    # no finding consumes text from a second sentence.
    for rule_id, pattern, message in RULES:
        for match in pattern.finditer(masked):
            line, column = location(match.start())
            end_line, end_column = location(match.end())
            findings.append({
                "rule_id": rule_id, "severity": "review",
                "line": line, "column": column,
                "end_line": end_line, "end_column": end_column,
                "match": text[match.start():match.end()],
                "message": message,
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
    parser.add_argument("--input-format", choices=("text", "markdown"),
                        help="Input interpretation (default: Markdown for .md/.markdown files, text otherwise)")
    parser.add_argument("--format", choices=("text", "json"), default="text", help="Output format (default: text)")
    parser.add_argument("--fail-on", choices=("review",), help="Return exit code 1 only when review findings exist")
    args = parser.parse_args(argv)
    source = args.file if args.file is not None else "<inline text>"
    input_format = args.input_format or (
        "markdown" if args.file and Path(args.file).suffix.lower() in (".md", ".markdown") else "text"
    )
    try:
        if args.file is not None:
            with open(args.file, encoding="utf-8-sig", newline="") as stream:
                text = stream.read()
        else:
            text = args.text
        diagnostics = []
        findings = scan_text(text, input_format=input_format, diagnostics=diagnostics)
    except (OSError, UnicodeError, ValueError) as error:
        parser.error(str(error))

    payload = {"source": source, "findings": findings,
               "summary": {"review": len(findings)}, "limitations": LIMITATIONS,
               "boundary_diagnostics": diagnostics}
    if args.format == "json":
        print(json.dumps(payload, ensure_ascii=True, indent=2))
    else:
        print(f"Source: {source}")
        for finding in findings:
            print(f"[review] {finding['rule_id']} "
                  f"{finding['line']}:{finding['column']}-"
                  f"{finding['end_line']}:{finding['end_column']} "
                  f"{finding['match']!r}: {finding['message']}")
        for item in diagnostics:
            print(f"[boundary] {item['kind']} {item['line']}:{item['column']}-"
                  f"{item['end_line']}:{item['end_column']}: {item['message']}")
        print(f"Review findings: {len(findings)} (advisory; human judgment required).")
        for limitation in LIMITATIONS:
            print(f"Limitation: {limitation}")
    return 1 if args.fail_on == "review" and findings else 0


if __name__ == "__main__":
    sys.exit(main())
