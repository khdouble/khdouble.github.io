"""Copy the authoritative CV into files/ before each render.

The CV is maintained in Word and exported to a fixed path on the author's
machine, always under the same filename. That exported PDF — not the copy in
this repository, and not any Google Drive share link — is the source of truth:

    E:/GoogleDrive/106_Research/89_JobMarket/CV_HyunHak_Kim.pdf

So `quarto render` picks up whatever was last exported, and the published CV
cannot silently fall behind.

If the source is missing (a build on any other machine, or in CI) the script
says so and exits cleanly, leaving the committed copy in place. It refuses to
copy anything that is not a PDF.
"""

import filecmp
import shutil
import sys
from pathlib import Path

SOURCE = Path("E:/GoogleDrive/106_Research/89_JobMarket/CV_HyunHak_Kim.pdf")
TARGET = Path(__file__).parent / "files" / "cv-hyunhak-kim.pdf"


def main() -> int:
    if not SOURCE.is_file():
        print(f"sync_cv: source not found, keeping the committed copy ({SOURCE})")
        return 0

    with SOURCE.open("rb") as fh:
        if fh.read(4) != b"%PDF":
            print(f"sync_cv: {SOURCE} is not a PDF — refusing to copy", file=sys.stderr)
            return 1

    if TARGET.is_file() and filecmp.cmp(SOURCE, TARGET, shallow=False):
        print("sync_cv: CV unchanged")
        return 0

    TARGET.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SOURCE, TARGET)
    print(f"sync_cv: CV updated from source ({TARGET.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
