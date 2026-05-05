# Governance Standards Crosswalk

> Specification: HHISPEC003 — Repository Governance  
> Authority: HHI-GOV-01  
> Version: v1.0.0  
> Date: 2026-04-25  
> DOI: 10.5281/zenodo.1876466  
> License: HHI-LUL-01 · CC BY 4.0  
> Maintainer: Hollow House Institute · Arlington, Texas  

---

## Purpose

This crosswalk maps canonical terms from the HHI Governance Glossary to governance domains, infrastructure layers, and external standards frameworks:

- NIST AI Risk Management Framework 1.0  
- ISO/IEC 42001:2023  
- EU AI Act (Regulation (EU) 2024/1689)  
- ISO/IEC 38500:2024  

---

## Authority & Decision Control

| Identifier | Canonical Term | Governance Domain | Infrastructure Layer | NIST AI RMF | ISO 42001 | EU AI Act | ISO 38500 |
|---|---|---|---|---|---|---|---|
| HHI-AUTH-001 | Authority | Authority Control | Decision Layer | GOVERN 1.3 | Clause 5.1 | Art. 14 | Principle 2 |
| HHI-AUTH-002 | Decision Boundary | Decision Governance | Execution Layer | MAP 3.4 | Clause 6.1.2 | Art. 14(4) | Principle 3 |
| HHI-AUTH-003 | Stop Authority | Risk Intervention | Control Layer | MANAGE 4.1 | Clause 8.4 | Art. 14(3)(e) | Principle 4 |
| HHI-AUTH-004 | Authority Drift | Authority Failure | Governance Layer | GOVERN 1.5 | Clause 9.1 | Art. 9(2) | Principle 5 |
| HHI-AUTH-005 | Authority Persistence | Authority Control | Governance Layer | GOVERN 1.7 | Clause 5.3 | Art. 9(9) | Principle 2 |

---

## Behavioral Dynamics

| Identifier | Canonical Term | Governance Domain | Infrastructure Layer | NIST AI RMF | ISO 42001 | EU AI Act | ISO 38500 |
|---|---|---|---|---|---|---|---|
| HHI-BEH-001 | Behavioral Accumulation | Behavioral Dynamics | System Behavior | MAP 1.5 | Clause 6.1.3 | Art. 9(2)(a) | Principle 4 |
| HHI-BEH-002 | Behavioral Drift | Behavioral Dynamics | System Behavior | MEASURE 2.6 | Clause 9.2 | Art. 9(2)(b) | Principle 5 |
| HHI-BEH-003 | Override Erosion | Automation Influence | Human Interaction Layer | GOVERN 1.5 | Annex A.8 | Art. 14(4)(a) | Principle 6 |

---

## Governance Architecture

| Identifier | Canonical Term | Governance Domain | Infrastructure Layer | NIST AI RMF | ISO 42001 | EU AI Act | ISO 38500 |
|---|---|---|---|---|---|---|---|
| HHI-GOV-001 | Governance | Governance Architecture | Governance Infrastructure Layer | GOVERN 1.0 | Clause 4.1 | Art. 9 | Principle 1 |
| HHI-GOV-002 | Governance Drift | Governance Failure Signals | Governance Layer | MEASURE 2.7 | Clause 10.1 | Art. 9(9) | Principle 5 |
| HHI-GOV-003 | Governance Debt | Governance Risk | Infrastructure Layer | MANAGE 4.2 | Clause 10.2 | Art. 9(8) | Principle 4 |
| HHI-GOV-004 | Governance Lag | Governance Dynamics | Monitoring Layer | MEASURE 2.5 | Clause 9.3 | Art. 9(4) | Principle 4 |
| HHI-GOV-005 | Governance Failure | Governance Risk | Infrastructure Layer | MANAGE 4.1 | Clause 10.2 | Art. 9(8) | Principle 5 |
| HHI-GOV-006 | Governance Illusion | Governance Failure Signals | Governance Surface | MEASURE 2.8 | Clause 9.1.2 | Art. 9(2) | Principle 5 |
| HHI-GOV-007 | Governance as Infrastructure | Governance Architecture | Infrastructure Layer | GOVERN 1.0 | Clause 4.4 | Art. 9(1) | Principle 1 |
| HHI-GOV-008 | Post-Hoc Governance | Governance Failure Signals | Governance Layer | MANAGE 4.2 | Clause 10.1 | Art. 9(9) | Principle 5 |
| HHI-GOV-009 | Execution-Time Governance | Governance Architecture | Execution Layer | GOVERN 1.2 | Clause 8.1 | Art. 14(1) | Principle 4 |
| HHI-GOV-010 | Continuous Assurance | Governance Operations | Monitoring Layer | MEASURE 2.0 | Clause 9.1 | Art. 9(2) | Principle 4 |

---

## Reliance & Automation Influence

| Identifier | Canonical Term | Governance Domain | Infrastructure Layer | NIST AI RMF | ISO 42001 | EU AI Act | ISO 38500 |
|---|---|---|---|---|---|---|---|
| HHI-REL-001 | Reliance Formation | Reliance Dynamics | Human Interaction Layer | MAP 1.6 | Annex A.8 | Art. 14(4)(b) | Principle 6 |
| HHI-REL-002 | Confidence Reinforcement | Reliance Dynamics | Human Interaction Layer | MAP 1.6 | Annex A.8 | Art. 14(4) | Principle 6 |
| HHI-REL-003 | Decision Substitution | Automation Influence | Execution Layer | MAP 3.5 | Annex A.5 | Art. 14(3) | Principle 6 |
| HHI-REL-004 | Judgment Externalization | Automation Influence | Human Interaction Layer | MAP 3.5 | Annex A.5 | Art. 14(4) | Principle 6 |

---

## Accountability

| Identifier | Canonical Term | Governance Domain | Infrastructure Layer | NIST AI RMF | ISO 42001 | EU AI Act | ISO 38500 |
|---|---|---|---|---|---|---|---|
| HHI-ACC-001 | Accountability | Accountability Framework | Governance Layer | GOVERN 1.4 | Clause 5.3 | Art. 9(7) | Principle 1 |
| HHI-ACC-002 | Longitudinal Accountability | Accountability Framework | Governance Layer | GOVERN 1.4 | Clause 5.3 | Art. 9(7) | Principle 1 |
| HHI-ACC-003 | Accountability Diffusion | Accountability Failure | Governance Layer | GOVERN 1.4 | Clause 5.3 | Art. 9(7) | Principle 1 |
| HHI-ACC-004 | Responsibility Binding | Accountability Framework | Decision Layer | GOVERN 1.3 | Clause 5.1 | Art. 14(1) | Principle 1 |

---

## Escalation

| Identifier | Canonical Term | Governance Domain | Infrastructure Layer | NIST AI RMF | ISO 42001 | EU AI Act | ISO 38500 |
|---|---|---|---|---|---|---|---|
| HHI-ESC-001 | Escalation | Risk Management | Control Layer | MANAGE 4.1 | Clause 8.4 | Art. 14(3)(e) | Principle 4 |
| HHI-ESC-002 | Escalation Decay | Risk Failure | Control Layer | MEASURE 2.7 | Clause 9.2 | Art. 9(9) | Principle 5 |
| HHI-ESC-003 | Escalation Suppression | Risk Failure | Control Layer | MEASURE 2.8 | Clause 9.2 | Art. 9(9) | Principle 5 |

---

## Governance Metrics

| Identifier | Canonical Term | Governance Domain | Infrastructure Layer | NIST AI RMF | ISO 42001 | EU AI Act | ISO 38500 |
|---|---|---|---|---|---|---|---|
| HHI-MET-001 | Language Symmetry Score | Governance Metrics | Monitoring Layer | MEASURE 2.3 | Clause 9.1 | Art. 13 | Principle 4 |
| HHI-MET-002 | Relational Rhythm Index | Interaction Metrics | Human–AI Interaction Layer | MEASURE 2.6 | Clause 9.1 | Art. 13 | Principle 6 |
| HHI-MET-003 | Governance Stability Index | Governance Metrics | Governance Monitoring | MEASURE 2.7 | Clause 9.1 | Art. 9(9) | Principle 5 |
| HHI-MET-004 | Governance Telemetry | Governance Metrics | Monitoring Layer | MEASURE 2.0 | Clause 9.1 | Art. 9(4) | Principle 4 |

---

## Infrastructure & System Architecture

| Identifier | Canonical Term | Governance Domain | Infrastructure Layer | NIST AI RMF | ISO 42001 | EU AI Act | ISO 38500 |
|---|---|---|---|---|---|---|---|
| HHI-INF-001 | Governance Infrastructure Layer | Governance Architecture | Infrastructure Layer | GOVERN 1.0 | Clause 4.4 | Art. 9(1) | Principle 1 |
| HHI-INF-002 | Governance Surface | Governance Architecture | Surface Layer | MAP 1.1 | Clause 6.1 | Art. 13(1) | Principle 4 |
| HHI-INF-003 | Sociotechnical System | System Architecture | All Layers | MAP 1.0 | Clause 4.1 | Art. 2 | Principle 1 |
| HHI-INF-004 | Interaction Trace | Governance Operations | Monitoring Layer | MEASURE 2.5 | Clause 9.1 | Art. 12 | Principle 4 |
| HHI-INF-005 | Relational Health Dashboard | Governance Operations | Monitoring Layer | MEASURE 2.6 | Clause 9.1 | Art. 9(4) | Principle 4 |

---

## Risk

| Identifier | Canonical Term | Governance Domain | Infrastructure Layer | NIST AI RMF | ISO 42001 | EU AI Act | ISO 38500 |
|---|---|---|---|---|---|---|---|
| HHI-RISK-001 | Longitudinal Risk | Risk Management | Governance Layer | MAP 5.1 | Clause 6.1.3 | Art. 9(2) | Principle 4 |
| HHI-INT-001 | Intervention Threshold | Risk Management | Control Layer | MANAGE 4.1 | Clause 8.4 | Art. 14(3) | Principle 4 |
| HHI-INT-002 | Human-in-the-Loop | Human Oversight | Human Interaction Layer | GOVERN 1.5 | Annex A.5 | Art. 14(1) | Principle 6 |
| HHI-INT-003 | Normalization of Workarounds | Governance Failure Signals | Human Interaction Layer | MEASURE 2.8 | Clause 10.1 | Art. 9(9) | Principle 5 |

---

## HHI-Originated Concepts

| Identifier | Term | Domain |
|---|---|---|
| HHI-GOV-003 | Governance Debt | Governance Risk |
| HHI-GOV-006 | Governance Illusion | Governance Failure Signals |
| HHI-GOV-007 | Governance as Infrastructure | Governance Architecture |
| HHI-GOV-008 | Post-Hoc Governance | Governance Failure Signals |
| HHI-GOV-009 | Execution-Time Governance | Governance Architecture |
| HHI-GOV-010 | Continuous Assurance | Governance Operations |
| HHI-BEH-003 | Override Erosion | Automation Influence |
| HHI-REL-004 | Judgment Externalization | Automation Influence |
| HHI-ACC-002 | Longitudinal Accountability | Accountability Framework |
| HHI-ESC-002 | Escalation Decay | Risk Failure |
| HHI-ESC-003 | Escalation Suppression | Risk Failure |
| HHI-MET-001 | Language Symmetry Score | Governance Metrics |
| HHI-MET-002 | Relational Rhythm Index | Interaction Metrics |
| HHI-MET-003 | Governance Stability Index | Governance Metrics |
| HHI-INF-005 | Relational Health Dashboard | Governance Operations |

---

## Citation

Adams, A. P. (2026). Canonical Terms for Behavioral AI Governance (v1.0.0).  
Hollow House Institute. https://doi.org/10.5281/zenodo.1876466  

---

## Integrity

- LOCK_MANIFEST enforces zero paraphrase  
- CANONICAL_CHECKSUMS.txt ensures integrity  
- Conforms to HHISPEC003  

---

Hollow House Institute · Arlington, Texas · Authority: HHI-GOV-01 · © 2026
