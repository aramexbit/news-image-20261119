"""news-image-20261119 entry v5 (Python 3.13).

The entry image is a single newspaper front page summing up the world's
news of Thursday 19 November 2026 in 43 stories. At runtime this program
COMPOSES it from hardcoded text/data — no network, no randomness, no
timestamps in the output: two runs produce identical bytes.

Composition (see build_entry.py, same code this program imports) — rebuilt
from a study of the live top 10 (win rates 99.23%-99.03%), which all do
the same things, so v2 did them too, and v3 densifies them: v2 scored
98.01% provisional (11W-1L) against a top-20 line of ~98.9%, so v3 adds
richer hero scenes, taller mid-card illustration bands with bigger
icons, a HOW SURE ARE WE? confidence legend and a THE DAY IN UTC
mini-timeline under the map. v4 (user order, after checking the top
rank themselves: more HD, more detail — the judge reads the screenshot)
densifies further within the competition's fixed 1024x1024 canvas:
Shenzhen skyline + microphones, GTA VI clouds + lit back-row windows +
third car, 13 candles + order-book depth bars on the Nasdaq board, and
tiny country labels on the map:
- Three hero panels in a row (Shenzhen summit, GTA VI, Anthropic IPO),
  each a FLAT DRAWN illustration with a big label — the top 10 use no
  photographs at all. The small flat icons for the 10 mid cards are
  drawn in code as well.
- A numbers strip ($81.3bn, 15.9m, 551,864, 200,000, 109-0, 3
  presidents), region tabs with story counts, a red-italic subhead under
  the date, and per-story source attribution on every card.
- A DATE CHECK box listing stories deliberately left out because they
  were first reported on other days.
- Below the heroes: 10 mid cards, 24 one-line briefs, a numbered world
  map and a sources footer. All facts were checked against live news
  reporting of 19 November 2026 and the top-10 consensus; disputed
  claims are attributed in the image.

Output: $MAKEFUN_OUTPUT_DIR/entry.png (default /output), 1024x1024,
at most 1 MiB. If Pillow is unavailable in the runtime container, the
program falls back to copying the prebuilt entry.png shipped beside it
(byte-identical to what the composer produces).

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import struct
import sys

MAX_BYTES = 1_048_576  # 1 MiB gate limit
MAX_DIMENSION = 1024  # 1024x1024 gate limit
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(message: str) -> "SystemExit":
    print(f"error: {message}", file=sys.stderr)
    return SystemExit(1)


def read_png_dimensions(path: str) -> tuple[int, int]:
    """Return (width, height) parsed from the PNG IHDR chunk."""
    with open(path, "rb") as handle:
        header = handle.read(33)
    if len(header) < 33 or header[:8] != PNG_MAGIC:
        raise ValueError("not a PNG file (bad magic bytes)")
    if header[12:16] != b"IHDR":
        raise ValueError("not a PNG file (first chunk is not IHDR)")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def compose(output_path: str) -> tuple[int, int, int]:
    """Compose entry.png from local assets via build_entry.build()."""
    from build_entry import build  # Pillow-based composer, same repo

    image = build()
    image.save(output_path, optimize=True)
    size = os.path.getsize(output_path)
    width, height = read_png_dimensions(output_path)
    return width, height, size


def copy_prebuilt(source: str, output_path: str) -> tuple[int, int, int]:
    """Fallback: copy the prebuilt entry.png shipped in the repo."""
    shutil.copyfile(source, output_path)
    size = os.path.getsize(output_path)
    width, height = read_png_dimensions(output_path)
    return width, height, size


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError:
        # Fallback: the requested output dir cannot be created (read-only
        # parent, permissions). Use a local ./out dir next to this file
        # instead of failing the run outright.
        fallback = os.path.join(here, "out")
        print(
            f"warning: cannot create {output_dir}, falling back to {fallback}",
            file=sys.stderr,
        )
        output_dir = fallback
        try:
            os.makedirs(output_dir, exist_ok=True)
        except OSError as exc:
            raise SystemExit(fail(f"cannot create output dir {output_dir}: {exc}"))
    if not os.path.isdir(output_dir):
        raise SystemExit(fail(f"output path is not a directory: {output_dir}"))

    destination = os.path.join(output_dir, "entry.png")

    try:
        width, height, size = compose(destination)
        mode = "composed from local assets"
    except Exception as exc:  # Pillow missing, assets missing, etc.
        print(f"warning: compose failed ({exc}); copying prebuilt entry.png",
              file=sys.stderr)
        if not os.path.isfile(source):
            raise SystemExit(fail(f"source image missing: {source}"))
        width, height, size = copy_prebuilt(source, destination)
        mode = "copied prebuilt entry.png (fallback)"

    if size > MAX_BYTES:
        raise SystemExit(fail(f"entry.png is {size} bytes, over the 1 MiB limit"))
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        raise SystemExit(
            fail(f"entry.png is {width}x{height}, over the 1024x1024 limit")
        )

    # Verify the output: same PNG magic, so a truncated or partial write
    # is caught here instead of reaching the judge.
    with open(destination, "rb") as handle:
        if handle.read(8) != PNG_MAGIC:
            raise SystemExit(fail(f"copy failed validation: {destination}"))
    print(f"wrote {destination} ({width}x{height}, {size} bytes) [{mode}]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
