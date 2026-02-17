# SPEC-002
## Terminology Governance & Canonicalization

**Document ID:** HHI-SPEC-002  
**Version:** 1.0.0  
**Status:** Canonical  
**Applies To:** All terminology entries in Hollow House Institute standards and artifacts  
**Doctrine Anchor:** Time turns behavior into infrastructure.

---

## 1. Purpose

This specification defines the governance process for coining, defining, validating, and canonicalizing terminology used by Hollow House Institute.

Its purpose is to prevent:
- semantic drift
- synonym sprawl
- inference-to-fact naming
- person-targeting language
- non-repeatable term creation

---

## 2. Scope

This specification applies to:
- glossary entries (Markdown and JSON)
- audit terminology used in findings
- framework labels and classification names
- internal term proposals and provisional terms

This specification does not define:
- licensing terms (handled by the Master License Suite and HHI_LUL_01)
- implementation mechanics (handled by governance artifacts)

---

## 3. Term Status Levels

All terms must be assigned a status:

- **Provisional**: proposed but not yet validated in longitudinal use
- **Canonical**: approved, stable, and governed for reuse across artifacts
- **Deprecated**: retained only for historical continuity; not valid for new use

---

## 4. Term Coining Trigger Conditions

A term may be coined only when at least one condition is met:

- the phenomenon cannot be precisely named with existing terms
- existing language is ambiguous or creates category error
- repeated usage requires paragraph-length explanation without a stable noun
- the phenomenon appears repeatedly across audits, datasets, or governance artifacts

If none apply, the term must not be coined.

---

## 5. Required Coining Process (TERM-COIN-01)

### 5.1 Phenomenon Statement (Pre-Linguistic)
A phenomenon statement must be written before naming:

“This term exists to describe: ________.”

Constraints:
- no metaphors
- no moral judgment
- no solution language
- describe what happens over time

If the phenomenon cannot be stated, the process stops.

### 5.2 Boundary Definition
Each term must include an explicit boundary:

**IS**
- observable at organizational scale
- detectable longitudinally
- independent of intent
- compatible with audit evidence

**IS NOT**
- a personality trait
- a one-time failure
- a legal conclusion
- a synonym for an existing term

If overlap with an existing term is material, the term must be revised or aborted.

### 5.3 Naming Constraints
The coined name must:
- compress a paragraph into a stable noun
- be neutral in tone
- favor systems and patterns over people
- remain compatible with “over time” framing
- be suitable for audit findings

Avoid:
- pop-psych labeling
- metaphorical imagery
- trend vocabulary
- person-targeting terms

---

## 6. Canonical Definition Format

Canonical definitions must use:

“**TERM**: A [pattern/condition/process] in which ________, resulting in ________ over time.”

Constraints:
- one sentence
- no examples
- no prescriptions
- no implied intent

---

## 7. Drift Resistance Check

Each term must be evaluated for misuse risk:

- can it be weaponized against individuals?
- can it be misread as intent or motive?
- does it collapse into “bad behavior” when quoted?
- does it distort outside governance context?

If risk is non-trivial, the term must be tightened or renamed.

---

## 8. Canonicalization Criteria

A term becomes **Canonical** only if:
- used consistently in analysis or audits
- survives at least one longitudinal application
- reduces explanation length without loss of precision
- does not duplicate an existing term’s scope

Until then, it remains **Provisional**.

---

## 9. Required Outputs

For each Canonical term:
- glossary.md entry (canonical)
- glossary.json entry (if used by software)
- stable spelling and casing
- governance tier attribution (internal)

---

## 10. Enforcement

Any artifact that introduces terminology outside this process is considered governance drift and must be corrected.

---

**End of SPEC-002**
