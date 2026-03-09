---

# Glossary Infrastructure Specification

The HHI Governance Glossary functions as a canonical terminology registry supporting governance analysis, auditing, and system design.

To support interoperability across standards, audits, and machine-readable governance systems, the glossary includes a stable identifier system and optional structured metadata fields.

These elements allow glossary terms to function as governance infrastructure rather than simple documentation.

## Stable Term Identifiers

Each glossary entry may be assigned a permanent identifier.

Identifier structure:

HHI-[DOMAIN]-[NUMBER]

Example:

HHI-AUTH-003

Identifiers are permanent once assigned.

Identifiers are never reused, even if a term is retired.

Retired terms retain their identifier but may be marked as deprecated.

Identifiers allow governance documents, audits, and software systems to reference concepts without ambiguity.

## Domain Classification Codes

Glossary identifiers include a domain code representing the conceptual category of the term.

Current domain codes include:

AUTH — Authority and decision control  
BEH — Behavioral governance foundations  
GOV — Governance mechanisms and accountability  
RISK — Longitudinal risk and failure dynamics  
INT — Human–system interaction dynamics  
MET — Measurement constructs  
OPS — Operational monitoring systems  
SYS — Structural governance systems

Example identifiers:

HHI-AUTH-001 — Authority  
HHI-AUTH-002 — Decision Boundary  
HHI-AUTH-003 — Stop Authority  

HHI-BEH-001 — Behavioral Drift  
HHI-BEH-002 — Reliance Formation  

HHI-RISK-001 — Governance Lag  

The identifier remains stable regardless of definition updates.

## Structured Metadata Fields

Glossary entries may optionally include structured metadata to support governance analysis, auditing, and machine-readable interpretation.

Not all fields are required for every term.

Fields may be added progressively as the glossary evolves.

### Semantic Role

Describes the functional role a concept performs within governance systems.

Example roles:

authority — holds final decision power  
constraint — limits system behavior  
boundary — defines transition between actors  
observer — monitors system behavior  
executor — performs automated actions

### Governance Layer

Specifies where the concept operates within governance architecture.

Possible layers include:

language — conceptual terminology  
policy — organizational governance rules  
execution — runtime system governance  
audit — monitoring and verification mechanisms

### Control Type

Describes how the concept influences system behavior.

preventive — prevents governance failures before they occur  
detective — detects governance failures or drift  
corrective — enables remediation or intervention

### Risk Domain

Categorizes the governance risk addressed by the concept.

Possible domains include:

governance — authority and control structures  
reliability — system performance stability  
transparency — traceability and interpretability  
safety — prevention of harmful outcomes  
privacy — protection of sensitive information

### Lifecycle Phase

Indicates where in the system lifecycle the concept primarily applies.

design — system architecture and governance design  
development — system or model construction  
deployment — operational system behavior  
monitoring — post-deployment oversight

### Term Relationships

Glossary terms may reference other glossary entries to support semantic mapping.

Relationship types include:

parent_term — hierarchical concept relationship  
related_terms — associated governance concepts  
opposite_term — conceptual boundary

### Normative Status

Indicates whether the term represents enforceable governance requirements.

normative — required for governance compliance  
informational — descriptive or explanatory

### Drift Risk

Indicates likelihood of semantic drift across contexts.

low — meaning remains stable  
moderate — meaning may vary by domain  
high — meaning frequently shifts across disciplines

### Governance Stewardship

Glossary entries may include governance provenance metadata.

version_introduced — glossary version where the term first appeared  
last_reviewed — most recent governance review date  
steward — organization maintaining the definition

### External Framework References

Terms may optionally include mappings to external governance frameworks.

Examples include:

NIST AI Risk Management Framework  
ISO/IEC 42001 Artificial Intelligence Management Systems  
European Union Artificial Intelligence Act

External mappings support interoperability between HHI governance terminology and institutional governance standards.

## Purpose of Structured Terminology

Structured terminology enables the glossary to function as governance infrastructure.

This allows:

- stable conceptual references across standards and audits
- machine-readable governance analysis
- interoperability with regulatory frameworks
- long-term semantic stability

The glossary therefore acts as a foundational semantic layer supporting the broader Hollow House Institute governance architecture.
