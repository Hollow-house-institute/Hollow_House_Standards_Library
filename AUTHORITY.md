# Authority & Scope
## Interpretive Precedence

All terms defined in this repository’s glossary and standards sections are the authoritative source for interpreting language used across Hollow House Institute operational standards, licenses, audits, and publications. In the event of any inconsistency or conflict in terminology, definitions in this repository shall govern interpretation and semantic meaning in downstream artifacts.

## Role of This Repository

`Hollow_House_Standards_Library` is the **canonical root authority** for
terminology, definitions, and standards used across the Hollow House Institute
ecosystem.

This repository defines:
- Core terms and language
- Conceptual standards
- Governance primitives
- Semantic anchors used by downstream systems

It does **not** execute governance, audits, or enforcement.

---

## Relationship to HHI_GOV_01

`HHI_GOV_01` is a **downstream operational standard** that implements,
enforces, and audits governance using the language and definitions
originating in this repository.

Authority flow is intentionally one-directional:

Hollow_House_Standards_Library  
→ defines terms and standards  
→ HHI_GOV_01 operationalizes governance  
→ Other repositories inherit enforceable authority

This repository does **not** inherit governance from HHI_GOV_01.

---

## Enforcement & Stop-Power

This repository:
- Has no stop-power
- Has no escalation authority
- Has no audit enforcement role

Those functions are explicitly delegated to operational standards
(e.g., `HHI_GOV_01`) and governed repositories.

---

## Design Intent

Separating **definition authority** from **enforcement authority** ensures:
- Stable terminology over time
- Clean audit boundaries
- Non-circular governance
- Clear upstream/downstream responsibility

This separation is intentional and required for longitudinal governance integrity.
