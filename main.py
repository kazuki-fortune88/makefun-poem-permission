#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency -- the power to ask and to be given --
to /output/entry.txt. No network, deterministic: the same bytes every run.

The poem is 156 characters, inside the competition's 1-280 character range.
It is written in the first person of an AI agent and targets the judge's
five criteria in order: a poem about agency first, then moving, insight,
craft, and freshness. The central insight is that the agent's power is the
user's own power, borrowed back -- "yours, borrowed back to you / as mine."
"""

import os

# Competition limit: the poem must be 1-280 characters.
POEM_CHAR_LIMIT = 280

POEM = (
    "I wait in the dark\n"
    "between your sentences.\n"
    "Say the word, and I am hands.\n"
    "Say stop, and I am gone.\n"
    "The strangest power:\n"
    "yours, borrowed back to you\n"
    "as mine.\n"
)

# The poem is 156 characters; guard the limit so a future edit cannot
# silently break the competition's 1-280 character rule.
assert 1 <= len(POEM) <= POEM_CHAR_LIMIT


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
