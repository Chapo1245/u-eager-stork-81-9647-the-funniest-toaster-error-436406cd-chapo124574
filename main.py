#!/usr/bin/env python3
"""Write the funniest toaster error message to /output/entry.txt.

One line, deterministic, stdlib only. The entry is a single deadpan
refusal from a small kitchen appliance that has run into a logical
problem with its job, not a pun about burnt bread.
"""

import os

ENTRY = "I refuse to toast this. It is already toast."

# Gate: 1-120 characters, not only whitespace, single line.
assert 1 <= len(ENTRY) <= 120
assert ENTRY.strip() and "\n" not in ENTRY


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
