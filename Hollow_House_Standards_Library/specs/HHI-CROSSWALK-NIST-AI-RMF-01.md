# HHI-CROSSWALK-NIST-AI-RMF-01
# Crosswalk: HHI Governance Infrastructure ↔ NIST AI RMF
# Hollow House Institute (HHI)
# AI Governance Glossary — Version 1.3.0 (Governance Freeze)

---
semantic_role: crosswalk
governance_layer: infrastructure
control_type: mapping
risk_domain: longitudinal
lifecycle_phase: execution
normative_status: canonical
drift_risk: medium
source_framework: NIST AI RMF 1.0
identifier: HHI-CROSSWALK-NIST-AI-RMF-01
---

## Purpose
This crosswalk aligns key HHI governance primitives with the structural expectations of the NIST AI Risk Management Framework (AI RMF 1.0).  
All HHI terms use exact definitions from the **AI Governance Glossary**.

---

# Crosswalk Table

| HHI Canonical Term | Identifier | Exact Glossary Definition | NIST AI RMF Category | Alignment Notes |
|--------------------|------------|---------------------------|----------------------|-----------------|
| Governance Infrastructure Layer | HHI-GOV-020 | "Structural components enforcing governance rules." | GOVERN | Defines the structural layer NIST assumes but does not specify. |
| Execution-Time Governance | HHI-GOV-019 | "Governance mechanisms operating during system execution." | MAP / MEASURE / MANAGE | Provides real-time enforcement missing in NIST. |
| Behavioral Drift | HHI-BEH-001 | "Gradual divergence between expected system behavior and observed behavior over time." | MEASURE | Directly corresponds to drift monitoring. |
| Authority | HHI-AUTH-002 | "The formally assigned right to make, override, pause, or stop decisions during execution." | GOVERN | Clarifies decision rights NIST leaves implicit. |
| Decision Boundary | HHI-AUTH-001 | "The explicit point at which authority transfers between actors during execution." | GOVERN | Defines authority transitions absent in NIST. |
| Governance Telemetry | HHI-GOV-018 | "Operational signals measuring governance performance." | MEASURE | Provides measurable governance signals. |
| Longitudinal Risk | HHI-RISK-001 | "Risk emerging through repeated behavior over time rather than discrete events." | MANAGE | Extends NIST risk framing into temporal accumulation. |

---

## Glossary Repository Reference
All terms are defined in the **AI Governance Glossary** (`glossary.json`) within the Hollow House Institute Standards Library.

## Glossary Version Authority
AI Governance Glossary — Version 1.3.0 (Governance Freeze)
