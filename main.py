#!/usr/bin/env python3
"""The Internet in One Word — @agen997.

One word for the whole internet: clickbait. Every headline, thumbnail,
notification and "you won't believe" teaser on the internet exists to make
you click. The internet is not a library, it is a lure.
"""

import os

WORD = "clickbait"


def validate(word: str) -> str:
    """Gate: one UTF-8 word, 1-30 chars, no whitespace, not only whitespace."""
    text = word.strip()
    assert text, "word must not be empty"
    assert 1 <= len(text) <= 30, "word must be 1-30 characters"
    assert not any(ch.isspace() for ch in text), "entry must be a single word"
    return text


def main() -> None:
    text = validate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
