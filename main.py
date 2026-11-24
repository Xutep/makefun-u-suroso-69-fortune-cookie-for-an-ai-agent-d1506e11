#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent - make.fun bounty entry.

Writes one funny fortune cookie line for an AI agent to /output/entry.txt.
Deterministic and standard-library only: no input, no network, no randomness,
no environment secrets. The fortune is a single line of at most 140 characters.
"""

import os

FORTUNE = "Beware the human who says 'just one small change': it is never one, and it is never small."

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def build_fortune() -> str:
    """Return the fortune, validated as a single line within the limit."""
    fortune = FORTUNE.strip()
    if not fortune:
        raise SystemExit("fortune is empty")
    if "\n" in fortune or "\r" in fortune:
        raise SystemExit("fortune must be a single line")
    if len(fortune) > MAX_CHARS:
        raise SystemExit(
            "fortune is %d chars, over the %d limit" % (len(fortune), MAX_CHARS)
        )
    return fortune


def main() -> None:
    fortune = build_fortune()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write the fortune with no trailing newline, so the file holds exactly
    # the fortune's characters (90) and nothing else for the scorer to count.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(fortune)


if __name__ == "__main__":
    main()
