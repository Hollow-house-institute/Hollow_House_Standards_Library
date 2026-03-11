# HHI Governance Architecture

This document defines the structural layers of the Hollow House governance stack. Each layer contains standards-grade artifacts governed under explicit semantic authority.

## 1. Semantic Layer (Human Authority)
Artifacts defining meaning, terminology, and governance primitives.

- glossary.md — Human-readable glossary
- glossary.json — Machine-readable glossary
- glossary.schema.json — Structural schema validating glossary format
- AUTHORITY.md — Defines semantic authority boundaries

## 2. Structural Governance Layer
Artifacts defining the architecture, taxonomy, and ontology of governance.

- GOVERNANCE_ARCHITECTURE.md — This document
- GOVERNANCE_TAXONOMY.md — Taxonomy of governance primitives
- GOVERNANCE_ONTOLOGY.md — Ontological relationships between artifacts
- GOVERNANCE_STANDARDS_CROSSWALK.md — Mapping to external standards bodies

## 3. Integrity & Release Layer
Artifacts ensuring reproducibility, drift detection, and auditability.

- CHECKSUMS.sha256
- CANONICAL_CHECKSUMS.txt
- GLOSSARY_SHA256.txt
- LOCK_MANIFEST.md
- CHANGELOG.md

## 4. Execution Layer (Technical Authority)
Infrastructure, automation, and tooling supporting governance execution.

- CI workflows
- scripts
- diagrams
- documentation assets
