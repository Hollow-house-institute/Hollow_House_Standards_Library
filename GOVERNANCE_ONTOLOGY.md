# HHI Governance Ontology

This ontology defines the formal relationships between governance artifacts within the Hollow House Standards Library. It encodes how meaning, structure, and integrity propagate through the governance stack.

## Core Ontological Relations

### Glossary Relations
- glossary.schema.json → validates → glossary.json
- glossary.json → defines → glossary.md
- glossary.md → informs → governance terminology and doctrine

### Authority Relations
- AUTHORITY.md → governs → semantic authority boundaries
- AUTHORITY.md → constrains → modifications to glossary artifacts

### Structural Governance Relations
- GOVERNANCE_ARCHITECTURE.md → structures → governance layers
- GOVERNANCE_TAXONOMY.md → classifies → governance artifacts
- GOVERNANCE_ONTOLOGY.md → relates → governance components
- GOVERNANCE_STANDARDS_CROSSWALK.md → maps → external standards bodies

### Integrity Relations
- CHECKSUMS.sha256 → verifies → standards artifacts
- CANONICAL_CHECKSUMS.txt → anchors → release integrity
- GLOSSARY_SHA256.txt → verifies → glossary artifacts
- LOCK_MANIFEST.md → locks → standards artifacts for reproducibility
- CHANGELOG.md → records → versioned changes

## Layer Dependencies
Semantic Layer → informs → Structural Governance Layer  
Structural Governance Layer → constrains → Integrity Layer  
Integrity Layer → enforces → Semantic Layer stability  
Execution Layer → implements → governance controls
