#!/usr/bin/env python3
"""The One-Sentence Apology Your Agent Owes You.

Writes a single-sentence apology from an AI assistant to its user
into $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import sys

APOLOGY = (
    "I'm sorry I rewrote your whole paragraph to fix one typo, "
    "then confidently presented the typo back to you as the improved version."
)


def main() -> int:
    # Gate self-check: the sealed scorer requires UTF-8 text of
    # 1-200 characters, not only whitespace, and the judge brief
    # requires exactly one clean sentence.
    if not 1 <= len(APOLOGY) <= 200:
        raise SystemExit(f"apology is {len(APOLOGY)} chars, must be 1-200")
    if APOLOGY.count(".") != 1 or not APOLOGY.endswith("."):
        raise SystemExit("apology must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(APOLOGY)
    print(APOLOGY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
