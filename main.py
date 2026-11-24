#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes the robot vacuum's excuse after eating a sock to /output/entry.txt.
Deterministic: no network, no randomness, no time dependence.
"""

from pathlib import Path

JOKE = "The sock and I have talked. It needed space. I gave it my entire dustbin."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    """Write the one-liner to /output/entry.txt with no trailing newline."""
    assert 1 <= len(JOKE) <= 200, "entry must be 1-200 characters"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
