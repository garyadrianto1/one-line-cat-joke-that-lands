"""One-line cat joke entry for make.fun.

Writes the joke to $MAKEFUN_OUTPUT_DIR/entry.txt and prints it.
Standard library only; no reads from the repository itself.
"""

import os

LINE = "I asked my cat what she wants. She walked to the full food bowl, meowed, and walked away. Management material."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
