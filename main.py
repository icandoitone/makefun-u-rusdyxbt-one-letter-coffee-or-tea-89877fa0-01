#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry program.

Writes exactly one letter, "A" (coffee), to /output/entry.txt
(or to $OUTPUT_PATH when it is set). Standard library only,
no network access, no randomness, fully deterministic.
"""

import os
import sys

LETTER = "A"  # A = coffee, B = tea


def main() -> int:
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # Exactly one character, no trailing newline: the gate requires
    # /output/entry.txt to be UTF-8 text of 1 to 1 characters.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Read back and verify the gate condition ourselves: exactly one
    # UTF-8 character, not whitespace. Fail loudly if it ever drifts.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if len(written) != 1 or written.isspace():
        print(f"error: output is not exactly one letter: {written!r}",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
