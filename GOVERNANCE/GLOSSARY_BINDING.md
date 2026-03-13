# Glossary Binding

This document defines the canonical glossary state bound to the governance standard **HHI_GOV_01**.

The binding ensures that governance execution references a stable vocabulary and prevents semantic drift between governance logic and terminology definitions.

---

## Bound Glossary

Repository: Hollow House Standards Library  
File: glossary.json  
Version: v1.2.0  

SHA256:
9b3103a8f6df595e914b6abb728d68276babd51926ea9c243dcf4a25380a9f07

---

## Binding Rules

1. Governance execution MUST reference this glossary version and checksum.
2. Any glossary modification requires:
   - updated checksum
   - updated binding record
   - governance review prior to execution.
3. If the glossary checksum differs from the bound value, governance execution MUST be considered invalid until reconciliation occurs.

---

## Purpose

The glossary binding provides semantic integrity for governance infrastructure by ensuring that governance logic and terminology remain synchronized over time.
