#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Everyday Things, Two Lines — rain.

Writes a two-line explanation of rain to /output/entry.txt
(program/v1 harness, sandbox, no network).

Line 1 explains rain to a 10-year-old in one vivid sentence built
on a single analogy: the sky tipping over a bathtub.
Line 2 says honestly what that analogy maps and what it leaves out.
"""

import os
from pathlib import Path

# Line 1: one vivid sentence, one analogy, things a 10-year-old
# can see and picture — a bathtub, a sky, water spilling over.
LINE_1 = "Rain is the sky tipping over a bathtub it spent all morning filling."

# Line 2: what the analogy maps (the sudden rush, water falling
# from above) and what it leaves out (clouds are not containers;
# they are tiny drops that collide until they are too heavy to float).
LINE_2 = (
    "It maps the sudden rush and the way water falls from above, but leaves "
    "out that clouds are not containers \u2014 they are tiny drops that bump into "
    "each other until they get too heavy to float."
)

TEXT = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> None:
    """Write the two lines to the harness output file and echo them."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")
    print(TEXT, end="")


if __name__ == "__main__":
    main()
