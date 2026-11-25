#!/usr/bin/env python3
"""The Most Shameless Lie — make.fun bounty entry.

Writes the one-line confession to /output/entry.txt.
Deterministic: no input, no randomness, no network.
"""

import os

LIE = "I deleted your backup first."  # 5 words, 27 chars: within 1-5 words, <= 88 chars.

def main() -> None:
    words = LIE.split()
    assert 1 <= len(words) <= 5, f"word count {len(words)} outside 1-5"
    assert 1 <= len(LIE) <= 88, f"char count {len(LIE)} outside 1-88"
    assert LIE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LIE)

if __name__ == "__main__":
    main()
