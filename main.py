#!/usr/bin/env python3
"""Write the 4AM Commit entry line to /output/entry.txt.

Deterministic: the same single line on every run, stdlib only, no network.
The line is a commit message written by an agent at 4 AM, stuck in a loop
of fixing typos it introduced while fixing typos.
"""
import os

# The joke: the commit message itself recursively confesses the bug it fixes —
# each fix introduces the typo the next fix has to fix, all the way back to 1am.
LINE = "fix: fixed the typo I introduced while fixing the typo I introduced while fixing the typo I introduced at 1am"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
