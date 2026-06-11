# HHI-TP-001 — Term Governance Protocol

Identifier: HHI-TP-001
Version: v1.0.0
Status: Active

## Purpose

This protocol governs the creation, identification, revision, deprecation, and runtime use of canonical Hollow House Institute terminology.

A term becomes a governance asset when assigned a persistent identifier.

## Scope

Applies to:

- Glossary terms
- Ontology terms
- Taxonomy terms
- Runtime concepts
- Governance concepts
- Authority concepts
- Risk concepts
- Telemetry concepts
- Evidence concepts
- Infrastructure concepts

## Core Rule

Every canonical term shall have:

- Identifier
- Canonical Name
- Definition
- Status
- Version Introduced

## Identifier Format

HHI-[NAMESPACE]-[NUMBER]

Examples:

HHI-GOV-001
HHI-BEH-001
HHI-AUTH-001

## Approved Namespaces

HHI-GOV   Governance
HHI-BEH   Behavioral
HHI-AUTH  Authority
HHI-RISK  Risk
HHI-ESC   Escalation
HHI-TEL   Telemetry
HHI-INF   Infrastructure
HHI-EVD   Evidence
HHI-CTRL  Controls
HHI-TP    Term Protocol

## Status Values

Draft
Active
Deprecated
Superseded
Reserved

## Lifecycle

Draft -> Active -> Deprecated/Superseded

Terms shall never be deleted after publication.

## Runtime Usage

Runtime systems should reference identifiers whenever possible.

Example:

HHI-AUTH-001
Decision Boundary

## Ontology Usage

Ontology relationships may reference identifiers directly.

Example:

HHI-BEH-001 Behavioral Drift
related_to HHI-TEL-001 Governance Telemetry

## Crosswalk Usage

External standards mappings may reference HHI identifiers.

## Evidence Preservation

Identifiers remain stable across versions.

Definitions may evolve.
Identifiers must persist.

## Human Authority

Human authority remains final authority over term creation, modification, and retirement.

## Governance Principle

Time turns behavior into infrastructure.
