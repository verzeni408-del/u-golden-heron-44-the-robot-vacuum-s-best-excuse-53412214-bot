"""Robot vacuum excuse entry for make.fun.

Writes the one-line excuse to /output/entry.txt exactly, no trailing newline.
Entry is 95 characters, within the 140-character limit.
"""

import os
from pathlib import Path

ENTRY = "My cliff sensor mistook the dark rug for a staircase. I am not paid enough to fall down stairs."

# One line, one scene: cliff sensor vs dark rug, twist in the last sentence.
MAX_CHARS = 140


def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
