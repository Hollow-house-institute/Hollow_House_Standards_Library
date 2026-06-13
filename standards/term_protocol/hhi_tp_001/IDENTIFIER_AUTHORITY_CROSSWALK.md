# HHI Identifier Authority Crosswalk

Version: v1.0.0
Status: Draft

## Purpose

Maps legacy identifiers, registry identifiers, standards references, and supersession relationships for canonical HHI concepts.

| Canonical Concept | Legacy Identifier | Current Registry Identifier | Status |
|------------------|------------------|----------------------------|--------|
| Continuous Assurance | HHI-BEH-005 | HHI-CTRL-001 | Active Crosswalk |
| Continuous Assurance | HHI-GOV-011 | HHI-CTRL-001 | Superseded Reference |
| Runtime Governance | N/A | HHI-GOV-002 | Active |
| Behavioral Governance | N/A | HHI-GOV-003 | Active |
| Governance Observability | N/A | HHI-TEL-002 | Active |
| Telemetry Continuity | N/A | HHI-TEL-003 | Active |
| Governance Event | N/A | HHI-EVD-002 | Active |
| Authority Stack | N/A | HHI-AUTH-004 | Active |

## Resolution Rule

When multiple identifiers exist for the same concept:

1. Current Registry Identifier is authoritative.
2. Legacy identifiers remain valid for historical traceability.
3. Crosswalk mappings preserve replayability and provenance.
4. Superseded identifiers SHALL NOT be assigned to new artifacts.

