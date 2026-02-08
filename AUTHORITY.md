# Authority Model

This repository separates semantic authority from execution and review functions.

## Canonical Semantic Authority
**HHIHumanAuthority** is the sole authority for:
- glossary.json
- governance definitions
- semantic versioning of standards

Only this authority may define, modify, or lock meaning.

## Execution & Tooling Authority
**hhidatasettechs** maintains:
- tooling
- pipelines
- datasets
- renderers
- validation and enforcement mechanisms

This role may not redefine or extend semantic assets.

## Review Authority
**hhireviewauthority** performs:
- audit review
- compliance verification
- governance assessment

This role is non-authoritative and non-modifying.

## Platform Roles
GitHub organization roles (e.g. Owner) do not imply semantic authority.
Authority is defined by this document and enforced by practice.
