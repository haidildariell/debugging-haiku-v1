#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — one haiku, 5-7-5, plain text.

The haiku is held as three plain strings so the output is exactly the
poem: no title, no extra blank lines, no trailing commentary.
"""

import os
from pathlib import Path

LINES = [
    "Flaky test turns green",
    "on retry, no code has changed",
    "luck wears a lab coat",
]

# Syllable counts, verified by hand: 5 / 7 / 5.
# Flak-y(2) test turns green = 5; on re-try(2) no code has changed = 7;
# luck wears a lab coat = 5. Total 75 characters including newlines.


def build_haiku() -> str:
    if len(LINES) != 3:
        raise ValueError("a haiku needs exactly three lines")
    text = "\n".join(LINES) + "\n"
    if len(text) > 200:
        raise ValueError("haiku exceeds 200 characters")
    return text


def main() -> None:
    output_dir = os.environ.get("ENTRY_OUTPUT_DIR") or "/output"
    target = Path(output_dir) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(build_haiku(), encoding="utf-8")


if __name__ == "__main__":
    main()
