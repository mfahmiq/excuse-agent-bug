#!/usr/bin/env python3
"""Write the competition entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

Competition: u-kevin-the-excuse-your-agent-gives-you-c1861261
"The Excuse Your Agent Gives You" — one line, under 200 characters,
that an AI agent would hand its human after shipping a bug.
"""

import os

ENTRY = "The compiler warned me three times, but I read them as encouragement."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
