#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply (make.fun).

Writes the entry -- one original line -- to /output/entry.txt,
where the sealed scorer reads it.
"""

import os

ENTRY = "I'm out of the office until Monday; your email has been forwarded to my houseplant, which is also ignoring it."


def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
