#!/usr/bin/env python3
"""Convert source horse photos to optimised JPGs for the site."""

from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIRS = [
    ROOT / "images" / "source",
    ROOT / "images" / "_incoming",
    Path("/opt/cursor/artifacts/assets"),
]
OUTPUT_DIR = ROOT / "images"
MAX_WIDTH = 1600
QUALITY = 85
EXTS = {".jpg", ".jpeg", ".png", ".webp", ".heic", ".heif", ".bmp", ".tif", ".tiff"}


def collect_sources():
    seen = set()
    files = []
    for directory in SOURCE_DIRS:
        if not directory.is_dir():
            continue
        for path in sorted(directory.iterdir()):
            if not path.is_file():
                continue
            if path.suffix.lower() not in EXTS:
                continue
            key = path.resolve()
            if key in seen:
                continue
            seen.add(key)
            files.append(path)
    return files


def convert_one(src: Path, dest: Path):
    with Image.open(src) as img:
        img = ImageOps.exif_transpose(img)
        if img.mode not in ("RGB", "L"):
            img = img.convert("RGB")
        elif img.mode == "L":
            img = img.convert("RGB")

        if img.width > MAX_WIDTH:
            ratio = MAX_WIDTH / img.width
            img = img.resize((MAX_WIDTH, int(img.height * ratio)), Image.Resampling.LANCZOS)

        dest.parent.mkdir(parents=True, exist_ok=True)
        img.save(dest, "JPEG", quality=QUALITY, optimize=True, progressive=True)
    print(f"Wrote {dest.relative_to(ROOT)} ({dest.stat().st_size // 1024} KB)")


def main():
    sources = collect_sources()
    if not sources:
        print("No source images found. Add photos to images/source/ and run again.")
        return 1

    for index, src in enumerate(sources[:4], start=1):
        convert_one(src, OUTPUT_DIR / f"dompero-z-{index}.jpg")

    print(f"Converted {min(len(sources), 4)} photo(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
