"""One-star cat review entry.

Writes a single-line one-star review, written by a house cat about its
human, to /output/entry.txt. The text must be plain ASCII, one line,
1-200 characters.
"""

REVIEW = "One star. She works from home but bans me from her laptop, so I sat on the keyboard, resigned on her behalf, and kept the job. She cried."


def main():
    text = REVIEW.strip()
    # Self-check mirrors the sealed scorer (1-200 chars, not only
    # whitespace, plain ASCII, a single line) so an invalid entry is
    # never written.
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert all(ord(c) < 128 for c in text), "entry must be plain ASCII"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
