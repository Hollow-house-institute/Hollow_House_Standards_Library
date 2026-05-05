# HHI Decision Boundary Map

## What Is Happening

AI systems are being allowed to act before Authority, Accountability, Escalation, and Stop Authority are proven active.

This produces Behavioral Drift, Governance Lag, and Governance Illusion.

## Why It Fails

The system lacks an execution-time Decision Boundary. Governance exists as documentation, but not as control.

## What HHI Introduces

HHI introduces a Decision Boundary that must be checked before action.

| Boundary ID | Condition | Allow | Escalate | Stop Authority |
|---|---|---|---|---|
| DB-001 | Canonical terminology aligned | Yes | If ambiguous | If terminology drifts |
| DB-002 | Authority chain present | Yes | If incomplete | If unverifiable |
| DB-003 | Accountability bound to actor | Yes | If shared ownership | If no owner exists |
| DB-004 | Governance Telemetry produced | Yes | If partial | If absent |
| DB-005 | Human-in-the-Loop available | Yes | If delayed | If bypassed |

## Failure → Control Mapping

| Failure Pattern | Missing Capability | HHI Control | Evidence Produced |
|---|---|---|---|
| Behavioral Drift | Continuous Assurance | Governance Telemetry | Governance Telemetry Log |
| Decision Substitution | Decision Boundary | Stop Authority | Decision Boundary Map |
| Accountability Diffusion | Responsibility Binding | Interaction Trace | Escalation / Incident Log |
| Governance Lag | Execution-Time Governance | Continuous Assurance | Audit Proof |
| Governance Illusion | Governance Infrastructure Layer | Stop Authority | Evidence Package |

## What Becomes Visible

- whether action was allowed
- whether Escalation was required
- whether Stop Authority was triggered
- whether Accountability persisted
- whether Governance Telemetry exists

## Business Impact

| Role | HHI Value |
|---|---|
| CTO | System reliability and control |
| CFO | Financial risk containment |
| Legal | Liability traceability |
| Risk | Continuous Assurance |
| Operations | Decision clarity |

## Authority References

Canonical Source: https://github.com/hhidatasettechs-oss/Hollow_House_Standards_Library  
DOI: https://doi.org/10.5281/zenodo.1876466  
ORCID: https://orcid.org/0009-0009-4806-1949
