#!/data/data/com.termux/files/usr/bin/bash
set -e

fail() {
  echo "HHI ALIGNMENT FAILURE: $1"
  exit 1
}

[ -f ORCID_AUTHORITY_RECORD.md ] || fail "Missing ORCID_AUTHORITY_RECORD.md"
[ -f LINKEDIN_AUTHORITY_POST.md ] || fail "Missing LINKEDIN_AUTHORITY_POST.md"
[ -f DOI_INDEX.md ] || fail "Missing DOI_INDEX.md"
[ -f SYSTEM_MAP.md ] || fail "Missing SYSTEM_MAP.md"
[ -f AUTHORITY_CHECKSUMS.sha256 ] || fail "Missing AUTHORITY_CHECKSUMS.sha256"

git ls-files | grep -qx "ORCID_AUTHORITY_RECORD.md" || fail "ORCID authority record not tracked"
git ls-files | grep -qx "LINKEDIN_AUTHORITY_POST.md" || fail "LinkedIn authority post not tracked"
git ls-files | grep -qx "DOI_INDEX.md" || fail "DOI_INDEX.md not tracked"
git ls-files | grep -qx "SYSTEM_MAP.md" || fail "SYSTEM_MAP.md not tracked"

grep -q "https://doi.org/10.5281/zenodo.1876466" DOI_INDEX.md || fail "DOI missing from DOI_INDEX.md"
grep -q "AUTHORITY_CHECKSUMS.sha256" DOI_INDEX.md || fail "Checksum binding missing from DOI_INDEX.md"
grep -q "Authority System Cross-Layer Visibility" SYSTEM_MAP.md || fail "SYSTEM_MAP authority injection missing"
grep -q "ORCID → DOI → DOI_INDEX → GitHub Release → Commit → Standards Library" SYSTEM_MAP.md || fail "Authority chain missing from SYSTEM_MAP.md"

sha256sum -c AUTHORITY_CHECKSUMS.sha256 || fail "Checksum verification failed"

echo "HHI AUTHORITY CHAIN VALIDATED"
