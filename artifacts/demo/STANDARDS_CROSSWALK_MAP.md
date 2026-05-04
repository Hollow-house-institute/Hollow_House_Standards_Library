# HHI Standards Crosswalk Map

## What Is Happening

AI governance is fragmenting across standards, laws, internal policies, and vendor claims.

Organizations may reference ISO 42001, NIST AI RMF, and the EU AI Act, but still lack execution-time proof that Decision Boundary, Stop Authority, Accountability, Escalation, and Governance Telemetry are active.

This produces Governance Illusion, Governance Lag, and Longitudinal Risk.

## Why It Fails

Most governance programs map requirements to documents.

They do not map requirements to execution controls.

That leaves a missing Governance Infrastructure Layer between policy and behavior.

## What HHI Introduces

HHI introduces a crosswalk that binds external requirements to operational controls:

- Decision Boundary
- Stop Authority
- Governance Telemetry
- Interaction Trace
- Continuous Assurance
- Responsibility Binding
- Escalation

## Standards Crosswalk

| HHI Control | ISO 42001 Alignment | NIST AI RMF Alignment | EU AI Act Alignment | Evidence Produced |
|---|---|---|---|---|
| Decision Boundary | AI management system control point | Govern, Map, Manage | Human oversight and risk controls | Decision Boundary Map |
| Stop Authority | Corrective action and operational control | Manage | Human oversight and risk mitigation | Stop Authority Record |
| Governance Telemetry | Monitoring, measurement, evaluation | Measure, Manage | Logging and recordkeeping | Governance Telemetry Log |
| Interaction Trace | Documented operational evidence | Govern, Measure | Technical documentation and traceability | Interaction Trace |
| Continuous Assurance | Ongoing monitoring and improvement | Measure, Manage | Post-market monitoring logic | AI Risk Register |
| Responsibility Binding | Roles, responsibilities, accountability | Govern | Provider and deployer accountability | Accountability Record |
| Escalation | Nonconformity and corrective action | Manage | Incident handling and risk response | Escalation / Incident Log |

## Failure → Control Mapping

| Failure Pattern | Missing Capability | HHI Control | Evidence Produced |
|---|---|---|---|
| Governance Illusion | Execution-Time Governance | Decision Boundary | Decision Boundary Map |
| Behavioral Drift | Continuous Assurance | Governance Telemetry | Governance Telemetry Log |
| Accountability Diffusion | Responsibility Binding | Interaction Trace | Accountability Record |
| Governance Lag | Runtime monitoring | Continuous Assurance | AI Risk Register |
| Escalation Suppression | Intervention Threshold | Stop Authority | Escalation / Incident Log |
| Authority Drift | Authority Persistence | Responsibility Binding | Authority Review Log |
| Decision Substitution | Human-in-the-Loop | Stop Authority | Stop Authority Record |

## What Becomes Visible

This crosswalk makes visible:

- which external requirement maps to which HHI control
- which artifact proves the control exists
- where policy stops and execution begins
- where Longitudinal Risk can accumulate
- whether governance is operational or Post-Hoc Governance

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
DOI: https://doi.org/10.5281/zenodo.18615600  
ORCID: https://orcid.org/0009-0009-4806-1949
