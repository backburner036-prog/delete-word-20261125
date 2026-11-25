"""Entry for the make.fun bounty "The Word You'd Delete From the Dictionary".

The bounty asks for a single word to erase from the dictionary forever.
The chosen word is supercalifragilisticexpialidocious: instantly recognised,
funny on its own sound, and deleting the longest, most famous unspellable
word is the joke itself — no explanation needed.

The program writes exactly that word (nothing else, no trailing newline)
to /output/entry.txt, after validating it against the harness gate:
UTF-8 text, 1-77 characters, no surrounding whitespace, no newlines.
"""

from pathlib import Path

TEXT = "supercalifragilisticexpialidocious"

OUTPUT = Path("/output/entry.txt")


def validate(text: str) -> None:
    """Reject anything the harness gate would reject."""
    if not text:
        raise ValueError("text must not be empty")
    if text != text.strip():
        raise ValueError("text must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("text must not contain a newline")
    if any(ch.isspace() for ch in text):
        raise ValueError("entry text must be a single word (no whitespace)")
    n = len(text.encode("utf-8"))
    if not 1 <= n <= 77:
        raise ValueError(
            f"text must be 1-77 characters (UTF-8), got {n} "
            f"— gate limit is 1-77 UTF-8 characters"
        )


def main() -> None:
    validate(TEXT)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(TEXT, encoding="utf-8")
    back = OUTPUT.read_text(encoding="utf-8")
    assert back == TEXT, "round-trip mismatch: file content differs from TEXT"
    print(f"wrote {len(TEXT)} characters to {OUTPUT}")


if __name__ == "__main__":
    main()
