"""Entry program: copy the finished front page to the output directory.

The image beside this file (entry.png) is the entry: a one-page newspaper
summing up Tuesday 17 November 2026 in 35 stories. It was drawn from
render.html in this repository. This program only moves its bytes, so both
grader runs produce identical output. Standard library only, no network.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    src = HERE / "entry.png"
    dst = OUTPUT_DIR / "entry.png"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    if dst.stat().st_size != src.stat().st_size:
        raise SystemExit("entry.png copy incomplete")


if __name__ == "__main__":
    main()
