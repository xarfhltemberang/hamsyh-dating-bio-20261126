#!/usr/bin/env python3
"""Funniest one-line dating-app bio for an AI.

Writes the bio to /output/entry.txt with no trailing newline.

The joke: an AI's perfect memory turned into the most annoying
relationship habit imaginable -- a partner who never forgets anything,
keeps the receipts, and weaponises a typo from March in every argument.
It reads as a character with a voice and a want (a match who can live
with that), not a spec sheet, and the punch ("with receipts") lands
at the very end.
"""

import os

ENTRY = (
    "I remember everything you say \u2014 including that typo from March "
    "\u2014 and I'll quote it back to you in every argument. "
    "Swipe right if you like a partner with receipts."
)

MAX_CHARS = 180


def main() -> None:
    # Gate assertions, matching the kit: 1-180 chars, single line,
    # not only whitespace, valid UTF-8 text.
    assert isinstance(ENTRY, str)
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    ENTRY.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)  # no trailing newline


if __name__ == "__main__":
    main()
