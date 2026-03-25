# Glossary Binding

This document defines the canonical glossary state bound to the governance standard HHI_GOV_01.

---

## Bound Glossary

Repository: Hollow House Standards Library  
File: glossary.json  
Version: v1.3.0  

SHA256:
6e6fbf9a101121f7f6f130f59cdf2cfcb702a28558517317ab35fbe047ec3c88

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
