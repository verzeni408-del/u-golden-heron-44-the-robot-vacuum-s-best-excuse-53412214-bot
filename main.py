#!/usr/bin/env python3
"""Robot vacuum excuse — round two.

The vacuum mapped a mirror as a solid wall, then apologised to it.
A mapping excuse with a clean twist at the end: the apology lands
on the wrong object, which is exactly the joke.
"""

from pathlib import Path

EXCUSE = "I mapped the spot as a wall. It was a mirror. I have apologized to the wall."

OUTFILE = Path("/output/entry.txt")


def save_excuse(text: str, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def main() -> None:
    save_excuse(EXCUSE, OUTFILE)


if __name__ == "__main__":
    main()
