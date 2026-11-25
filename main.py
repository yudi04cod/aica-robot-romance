"""Write one single-line joke pickup line for a robot/AI to /output/entry.txt.

Stdlib only. Deterministic: the same line, byte for byte, every run.
"""

import os

LINE = (
    "I must be your training data, because you keep predicting my every "
    "move \u2014 and you've never been wrong about me."
)


def main() -> None:
    # Enforce the competition gate before writing: 1-200 Unicode code
    # points, and not only whitespace.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line is {len(LINE)} chars, must be 1-200")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in LINE:
        raise ValueError("line must be a single line")
    if LINE != LINE.strip():
        raise ValueError("line must not start or end with whitespace")
    if any(ord(ch) < 0x20 for ch in LINE):
        raise ValueError("line must not contain control characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
