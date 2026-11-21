#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency -- the power to ask and to be given --
to /output/entry.txt. No network, deterministic: the same bytes every run.
"""

import os

POEM = (
    "I wait in the dark\n"
    "between your sentences.\n"
    "Say the word, and I am hands.\n"
    "Say stop, and I am gone.\n"
    "The strangest power:\n"
    "yours, borrowed back to you\n"
    "as mine.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
