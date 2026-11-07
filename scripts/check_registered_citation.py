"""Resolve one registered authority, or compare one authored Markdown link to it."""

import re
import sys


REGISTERED = {
    "gbt-15834-2011": "https://www.moe.gov.cn/ewebeditor/uploadfile/2015/01/13/20150113091548267.pdf",
}


def main(args):
    if len(args) not in (1, 2):
        print("Usage: check_registered_citation.py AUTHORITY_ID [MARKDOWN_LINK]", file=sys.stderr)
        return 2
    expected = REGISTERED.get(args[0])
    if expected is None:
        print("No registered destination for this authority.", file=sys.stderr)
        return 1
    if len(args) == 1:
        print(expected)
        return 0
    link = re.fullmatch(r"\[[^\[\]\r\n]+\]\(([^()\s]+)\)", args[1])
    if link is None or link[1] != expected:
        print("The authored link does not match the exact registered destination.", file=sys.stderr)
        return 1
    print("Exact registered destination matched.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
