#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path("~/HHI/Hollow_House_Standards_Library").expanduser()

CONSTITUTION_REGISTRY = ROOT / "constitution/HHI_CONSTITUTION_01/CONSTITUTION_REGISTRY.json"
CONTROL_REGISTRY = ROOT / "controls/HHI_CTRL_01/CONTROL_REGISTRY.json"

graph = {
    "graph_id": "HHI-GRAPH-02",
    "version": "1.0.0",
    "nodes": [],
    "edges": []
}

seen_nodes = set()
seen_edges = set()

def add_node(node_id, node_type, name, status="ACTIVE"):
    if node_id not in seen_nodes:
        graph["nodes"].append({
            "id": node_id,
            "type": node_type,
            "name": name,
            "status": status
        })
        seen_nodes.add(node_id)

def add_edge(source, target, relationship):
    key = (source, target, relationship)
    if key not in seen_edges:
        graph["edges"].append({
            "from": source,
            "to": target,
            "relationship": relationship
        })
        seen_edges.add(key)

# Stage 1: Constitutional primitives
with open(CONSTITUTION_REGISTRY, "r") as f:
    constitution = json.load(f)

for primitive in constitution.get("primitives", []):
    cp_id = primitive["id"]
    cp_name = primitive["name"]
    add_node(cp_id, "CP", cp_name)

# Stage 2: Controls + CP -> CTRL edges
with open(CONTROL_REGISTRY, "r") as f:
    controls = json.load(f)

for control in controls.get("controls", []):
    ctrl_id = control["id"]
    ctrl_name = control["name"]
    add_node(ctrl_id, "CTRL", ctrl_name)

    primitive_id = control.get("primitive") or control.get("constitutional_primitive")
    if primitive_id:
        add_edge(primitive_id, ctrl_id, "DEFINES")

# Fallback: derive CP -> CTRL edges from Constitution registry controls field
for primitive in constitution.get("primitives", []):
    cp_id = primitive["id"]
    for ctrl_id in primitive.get("controls", []):
        add_edge(cp_id, ctrl_id, "DEFINES")

with open("GRAPH_AUTO.json", "w") as f:
    json.dump(graph, f, indent=2)

print(f"Generated {len(graph['nodes'])} nodes")
print(f"Generated {len(graph['edges'])} edges")
