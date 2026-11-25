#!/usr/bin/env python3
"""Write the 4AM Commit entry line to /output/entry.txt.

Deterministic: the same single line on every run, stdlib only, no network.
"""
import os

LINE = "fix: fixed the typo I introduced while fixing the typo I introduced while fixing the typo I introduced at 1am"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
