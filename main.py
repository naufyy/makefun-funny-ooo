#!/usr/bin/env python3
"""The funniest out-of-office auto-reply entry for make.fun.

Writes the chosen reply to /output/entry.txt.
"""
import os

ENTRY = "I'm on leave until Monday. My replacement is a spreadsheet that has already filed two complaints about me."

def main():
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
