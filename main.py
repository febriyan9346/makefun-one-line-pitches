#!/usr/bin/env python3
"""One-line pitch entry for make.fun's A Day of One-Line Pitches.

Writes the pitch -- one sentence, at most 240 characters -- to
entry.txt in the output directory, for the house judge to compare.
"""

import os

PITCH = (
    "You already have the hard part, the idea, so tell it in plain words "
    "to an AI agent on make.fun tonight and try the working first version "
    "it builds before you can talk yourself out of it."
)


def main():
    # The gate: UTF-8 text of 1 to 240 characters, not only whitespace,
    # and the brief asks for exactly one sentence.
    assert 1 <= len(PITCH) <= 240, "pitch must be 1-240 characters"
    assert PITCH.strip() == PITCH, "pitch must not have outer whitespace"
    assert PITCH.endswith("."), "pitch must end with a period"
    assert ". " not in PITCH and "?" not in PITCH and "!" not in PITCH, (
        "pitch must be one sentence (note: the dot in make.fun is not "
        "a sentence break)"
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH)
    print("wrote %d characters to %s" % (len(PITCH), path))


if __name__ == "__main__":
    main()
