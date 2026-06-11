#!/usr/bin/env python3

import json

with open("GRAPH_AUTO.json") as f:
    graph = json.load(f)

nodes = {n["id"] for n in graph["nodes"]}

orphans = []

for node in graph["nodes"]:
    nid = node["id"]

    connected = any(
        e["from"] == nid or e["to"] == nid
        for e in graph["edges"]
    )

    if not connected:
        orphans.append(nid)

print("Nodes:", len(graph["nodes"]))
print("Edges:", len(graph["edges"]))
print("Orphans:", len(orphans))

for orphan in orphans:
    print("ORPHAN:", orphan)
