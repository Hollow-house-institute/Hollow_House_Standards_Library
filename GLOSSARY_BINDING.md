# GLOSSARY BINDING — TERMINOLOGY AUTHORITY

## Terminology Validation Requirements

All terminology validation MUST be performed against glossary.json as the machine-readable source of truth.

Auditors MUST:

- verify term.id consistency across artifacts
- reject usage of undefined terms
- flag synonym substitution where a canonical term exists

Any deviation from glossary.json constitutes a terminology integrity violation.

## Violation Severity Levels

- Critical: breaks canonical authority (must block merge)
- High: introduces structural risk
- Medium: reduces clarity or discoverability
- Low: stylistic inconsistency
