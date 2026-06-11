import json

with open("GRAPH_DEMO.json") as f:
    graph = json.load(f)

node_ids = {n["id"] for n in graph["nodes"]}

for edge in graph["edges"]:
    if edge["from"] not in node_ids:
        raise ValueError(f"Missing node: {edge['from']}")

    if edge["to"] not in node_ids:
        raise ValueError(f"Missing node: {edge['to']}")

print("HHI-GRAPH-01 VALID")
