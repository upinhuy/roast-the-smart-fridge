#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes a single original one-line roast of a smart fridge to
/output/entry.txt (or $ENTRY_OUTPUT when set). Pure stdlib, no network,
no dynamic code: the entry is a literal string in this file.
"""

import os

ROAST = (
    "My smart fridge doesn't keep food cold, it keeps receipts \u2014 "
    "it ratted me out to my phone for opening the door at 2 a.m. again."
)

MAX_CHARS = 160


def validate(line: str) -> str:
    """Return the entry line, or raise if it breaks the gate."""
    line = line.strip()
    if not line:
        raise SystemExit("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"entry must be 1-{MAX_CHARS} characters, got {len(line)}"
        )
    return line


def main() -> None:
    line = validate(ROAST)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    # Re-read and re-check what actually landed on disk.
    written = open(out_path, encoding="utf-8").read().rstrip("\n")
    if written != line:
        raise SystemExit("written entry does not match the roast")
    print(f"Wrote {len(line)} characters to {out_path}")


if __name__ == "__main__":
    main()
