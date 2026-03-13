# Hollow House Standards Library — LOCK MANIFEST

Version: v1.0.0  
Authority: Hollow House Institute  
Scope: Behavioral AI Governance  
Status: Release Integrity Specification

This manifest enumerates the standards-grade artifacts whose presence, structure, and integrity are locked for reproducible releases and governance auditability.

Artifacts listed here constitute the canonical governance specification of the Hollow House Standards Library. Any modification to these artifacts must be accompanied by a version update and checksum regeneration.

---

## Locked Artifacts

Semantic Layer
- glossary.md
- glossary.json
- glossary.schema.json
- AUTHORITY.md

Structural Governance Layer
- GOVERNANCE_ARCHITECTURE.md
- GOVERNANCE_TAXONOMY.md
- GOVERNANCE_ONTOLOGY.md
- GOVERNANCE_STANDARDS_CROSSWALK.md
- GOVERNANCE_METRICS.md
- GOVERNANCE_POSITIONING.md

Integrity & Release Layer
- CHECKSUMS.sha256
- CANONICAL_CHECKSUMS.txt
- GLOSSARY_SHA256.txt
- CHANGELOG.md

---

## Integrity Rules

Artifacts listed in this manifest must adhere to the following controls:

- Structural changes require a version increment.
- All releases must regenerate checksum artifacts.
- Artifact additions require manifest updates.
- Canonical glossary changes must update both human-readable and machine-readable formats.

These controls ensure reproducibility, semantic stability, and traceable governance releases.
