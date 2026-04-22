#!/data/data/com.termux/files/usr/bin/bash

TS=$(date -u +"%Y%m%d_%H%M%S")
OUT="audit_bundle_$TS"

mkdir -p "$OUT"
ls -la

cp -r GOVERNANCE "$OUT"/
cp -r .github "$OUT"/ 2>/dev/null || true
cp glossary.json CHECKSUMS.sha256 AUTHORITY.md "$OUT"/ 2>/dev/null || true
ls -R "$OUT"

# Hash only files (no directories)
find "$OUT" -type f -exec sha256sum {} \; > "$OUT/manifest.sha256"

zip -r "$OUT.zip" "$OUT" >/dev/null

echo "Audit bundle created: $OUT.zip"
