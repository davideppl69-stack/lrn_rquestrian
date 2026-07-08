#!/usr/bin/env bash
# Copy chat-uploaded photos from the cloud agent artifacts folder and optimise them.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PREFIX="${1:-dompero-z}"
COUNT="${2:-4}"
ASSETS="/opt/cursor/artifacts/assets"
INCOMING="$ROOT/images/_incoming"
SOURCE="$ROOT/images/source"

mkdir -p "$INCOMING" "$SOURCE"

shopt -s nullglob
files=("$ASSETS"/*.{jpg,jpeg,png,webp,heic,HEIC,JPG,JPEG,PNG,WEBP})
shopt -u nullglob

if ((${#files[@]} == 0)); then
  echo "No attachment images found in $ASSETS"
  exit 1
fi

cp -f "${files[@]}" "$INCOMING/"
python3 "$ROOT/scripts/process_dompero_photos.py" "$PREFIX" "$COUNT"
echo "Imported ${#files[@]} attachment(s) into images/${PREFIX}-*.jpg"
