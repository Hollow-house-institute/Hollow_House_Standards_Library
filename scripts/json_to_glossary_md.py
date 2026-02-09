#!/usr/bin/env python3
import json
from pathlib import Path

data = json.loads(Path("glossary.json").read_text(encoding="utf-8"))

metadata = data.get("metadata", {})
title = metadata.get("title", "HHI Governance Glossary")
tagline = metadata.get("tagline", [])
version_info = metadata.get("version", {})
version = version_info.get("value", version_info) if isinstance(version_info, dict) else version_info

lines = []
lines.append(f"# {title}\n\n")
for t in tagline:
    lines.append(f"**{t}**  \n")
lines.append("\n---\n\n")
lines.append("## Glossary\n\n")

for item in data.get("glossary", []):
    term = item.get("term", "").strip()
    definition = item.get("definition", "").strip()
    notes = item.get("notes", []) or []

    lines.append(f"### {term}\n")
    lines.append("**Definition:**  \n")
    lines.append(f"{definition}\n\n")
    if notes:
        lines.append("**Notes:**  \n")
        for n in notes:
            lines.append(f"- {n}\n")
        lines.append("\n")

if version:
    lines.append("---\n\n## Versioning\n\n")
    lines.append(f"Current version: **{version}**\n")

Path("glossary.md").write_text("".join(lines), encoding="utf-8")
