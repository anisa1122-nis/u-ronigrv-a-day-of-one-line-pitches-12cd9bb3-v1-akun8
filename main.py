#!/usr/bin/env python3
"""A Day of One-Line Pitches — one-sentence pitch entry.

Writes a single sentence (at most 240 characters) to /output/entry.txt.
The sentence convinces a friend who has never coded to let an AI agent
build their first app idea on make.fun.

Stdlib only, offline, deterministic: every run writes the same bytes.
"""

import os
from pathlib import Path

# The pitch: one sentence, plain words, no coding needed.
# Counted at 178 characters — inside the 1..240 window.
SENTENCE = (
    "That app idea you've been carrying around — just describe it "
    "in plain words and an AI agent on make.fun will build a working "
    "first version you can actually try, no coding needed."
)


def output_dir() -> Path:
    """Where the grader expects the entry file.

    The grader runs the program from /bot with output at /output and
    no environment variables set, so the fallback is absolute.
    """
    return Path(os.environ.get("OUTPUT_DIR", "/output"))


def main() -> None:
    """Write the pitch sentence to entry.txt."""
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(SENTENCE, encoding="utf-8")


# Guard: only run when executed directly.
if __name__ == "__main__":
    main()
