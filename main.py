"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt and prints it.
"""

import os
import re

SENTENCE = (
    "Announcing his crackdown on crypto, the senator's slides would not "
    "convert to PDF, so he held his laptop up to the cameras and read the "
    "future of money off a phone photo of his own laptop screen."
)

MAX_CHARS = 320


def validate(sentence: str) -> None:
    """Enforce the competition's format rules for the entry sentence."""
    if not sentence or not sentence.strip():
        raise ValueError("sentence must not be empty or only whitespace")
    if sentence != sentence.strip():
        raise ValueError("sentence must not have leading or trailing whitespace")
    if len(sentence) > MAX_CHARS:
        raise ValueError(
            f"sentence is {len(sentence)} chars, over the {MAX_CHARS} limit"
        )
    if re.search(r"[\x00-\x1f\x7f]", sentence):
        raise ValueError("sentence must not contain newline/tab/control chars")
    if not sentence.endswith("."):
        raise ValueError("sentence must end with a period")
    if re.search(r"[.!?]\s", sentence):
        raise ValueError(
            "sentence must be a single sentence: no sentence-ending "
            "punctuation followed by whitespace inside it"
        )
    if sentence.count(".") != 1:
        raise ValueError("sentence must contain exactly one period, at the end")


def main() -> None:
    validate(SENTENCE)
    print(SENTENCE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
