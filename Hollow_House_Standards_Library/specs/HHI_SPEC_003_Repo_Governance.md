# SPEC-003
## Repository Governance & Authority Order

**Document ID:** HHI-SPEC-003  
**Version:** 1.0.0  
**Status:** Canonical  
**Applies To:** All Hollow House Institute repositories  
**Doctrine Anchor:** Time turns behavior into infrastructure.

---

## 1. Purpose

This specification defines the authority order, dependency constraints, and governance rules governing all Hollow House Institute repositories.

Its function is to:
- prevent semantic drift
- enforce scope boundaries
- preserve audit defensibility
- ensure licensing and authority integrity across the repository ecosystem

---

## 2. Authority Order (Non-Negotiable)

All repositories operate under the following order of authority:

1. Canonical Standards  
2. Governance Artifacts  
3. Licensing Artifacts  
4. Datasets & Evidence  
5. Education, Portfolio, and Public Interfaces

No repository may assert authority above its tier.

---

## 3. Repository Tiers & Roles

### Tier 0 — Canonical Authority
Defines meaning. No dependencies.
- Hollow_House_Standards_Library
- Master_License_Suite

Prohibitions:
- no operational guidance
- no audit conclusions
- no implementation logic

### Tier 1 — Governance Standards
Implements definitions. Enforces structure.
- HHI_GOV_01
- HHI_LUL_01
- HHI_Interaction_Controls
- Longitudinal_Behavioral_Governance

Constraints:
- must defer to Tier 0 for definitions
- may not redefine terms
- may not imply certification or approval

### Tier 2 — Reference & Research
Explains and contextualizes Tier 1.
- ai_governance_reference
- Longitudinal_AI_Governance_Whitepaper
- Research_Papers

Constraints:
- no new terminology
- no governance claims
- no prescriptive conclusions

### Tier 3 — Data Assets
Empirical evidence only.
- Datasets_Core
- Ai_Human_Relations_Datasets

Constraints:
- no normative language
- no conclusions
- no standalone interpretation

### Tier 4 — Education & Public Interface
Translation and demonstration only.
- Hollow_House_Academy
- HHI_Governance_Portfolio
- Hollow_House_Institute-site

Constraints:
- must link upstream
- cannot originate standards
- cannot imply enforcement authority

---

## 4. Dependency Rules

- dependencies flow downward only
- no circular references
- no downstream repository may redefine upstream content
- all definitions originate in Tier 0 only

Violation of dependency rules constitutes governance drift.

---

## 5. Required README Header (All Repos)

Every repository must include this header at the top of its README:

Role:  
Authority Tier:  
Depends On:  
Does Not Define:  
Governance Status:

---

## 6. Canonical Status

SPEC-003 is binding on:
- repository structure
- README language
- cross-repo references
- public claims
- licensing scope

No repository may opt out.

---

**End of SPEC-003**
