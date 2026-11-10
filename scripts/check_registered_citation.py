"""Resolve one registered authority, or compare one authored destination to it."""

import argparse
from html import unescape
import re
import sys


REGISTERED = {
    "gbt-15834-2011": "https://www.moe.gov.cn/ewebeditor/uploadfile/2015/01/13/20150113091548267.pdf",
}

# A single ordinary inline link. Angle markup and code spans in the label
# can change which link the reader sees or whether the outer link exists.
# Resolve those forms, reference links and escaped URLs before comparison.
INLINE_LINK = re.compile(
    r"\[(?P<label>[^\[\]<>`\\\r\n]+)\]\([ \t]*(?:<(?P<angle>[^<>()\\&\s]+)>|(?P<bare>[^<>()\\&\s]+))"
    r"""(?:[ \t]+(?:"[^"\\\r\n]*"|'[^'\\\r\n]*'|\([^()\\\r\n]*\)))?[ \t]*\)"""
)

# These Hangul fillers are letters in Unicode, but do not supply label text.
HANGUL_FILLERS = "\u115f\u1160\u3164\uffa0"


def has_label_text(label):
    return any(ch.isalnum() and ch not in HANGUL_FILLERS for ch in unescape(label))


def main(args):
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog="Pass one authored link per invocation. For other link syntaxes, "
        "resolve the effective href first and pass it as --destination.")
    parser.add_argument("authority_id")
    operand = parser.add_mutually_exclusive_group()
    operand.add_argument("markdown_link", nargs="?", help="one ordinary inline Markdown link")
    operand.add_argument("--destination", metavar="URL", help="one effective href, compared literally")
    options = parser.parse_args(args)
    expected = REGISTERED.get(options.authority_id)
    if expected is None:
        print("No registered destination for this authority.", file=sys.stderr)
        return 1
    if options.markdown_link is None and options.destination is None:
        print(expected)
        return 0
    actual = options.destination
    if options.markdown_link is not None:
        link = INLINE_LINK.fullmatch(options.markdown_link)
        if link is None or not has_label_text(link["label"]):
            print("Pass one simple inline link, or resolve the authored link and use --destination.",
                  file=sys.stderr)
            return 1
        actual = link["angle"] or link["bare"]
    if actual != expected:
        print("The authored link does not match the exact registered destination.", file=sys.stderr)
        return 1
    print("Exact registered destination matched.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
