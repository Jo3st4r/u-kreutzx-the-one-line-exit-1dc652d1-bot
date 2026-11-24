#!/usr/bin/env python3
"""The One-Line Exit — a one-line resignation letter.

Writes exactly one line (1-140 chars, UTF-8) to /output/entry.txt.

Beats:
  SETUP   — the job ad promised a "fast-paced environment"
  TWIST   — three years of sprinting on the job
  PUNCH   — still no finish line in sight
"""

import os

# --- beats ---------------------------------------------------------------
SETUP = "the ad said 'fast-paced environment'"
TWIST = "after three years of sprinting"
PUNCH = "I still can't see the finish line"

MAX_CHARS = 140


def entry_text():
    """Build the single resignation line from its beats."""
    return "I resign: {}, and {} {}.".format(SETUP, TWIST, PUNCH)


def validate(text):
    """The sealed scorer's gate: 1-140 chars, UTF-8, single line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    text.encode("utf-8")
    return True


def main():
    text = entry_text()
    validate(text)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
