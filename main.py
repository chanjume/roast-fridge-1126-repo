#!/usr/bin/env python3
"""Roast the Smart Fridge: one line, best laugh wins.

Writes a single roast line (<=160 chars) to /output/entry.txt.
The roast: the fridge nags about expired oat milk at 2:14 a.m.,
then reorders the very thing it just declared dead -- a specific,
real smart-fridge behaviour with a sting at the end.
"""

import os

ENTRY = "My smart fridge texted me at 2:14 a.m. that the oat milk expired \u2014 then ordered three more cartons of it."


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Verify the round-trip: what the judge reads must be exactly the entry.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "entry.txt round-trip mismatch"


if __name__ == "__main__":
    main()
