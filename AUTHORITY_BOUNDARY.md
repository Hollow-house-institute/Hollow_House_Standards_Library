# Authority Boundary — Hollow House Institute

## Canonical Authority (Read-Only)
The following files define governance, terminology, and authority.
They may be READ by tools and AI systems but may NOT be modified.

- glossary.md
- glossary.json
- AUTHORITY.md
- LICENSE.md
- SCOPE.md
- CANONICAL_CHECKSUMS.txt

These files are enforced as read-only at the filesystem and Git levels.

## Human Authority
Only the designated human maintainer may:
- Unlock canonical files
- Modify definitions
- Regenerate checksums
- Re-lock files after intentional change

## AI Role
AI systems:
- May read canonical files
- May reference definitions verbatim
- May NOT edit, rewrite, expand, summarize, or infer new definitions
- Have no stop authority
- Have no commit authority

## Enforcement
Authority is enforced by:
- File permissions (chmod 444)
- Git pre-commit hooks
- SHA-256 checksum verification

This boundary is non-negotiable.
