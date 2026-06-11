import json

with open("GRAPH_DEMO.json") as f:
    graph = json.load(f)

for edge in graph["edges"]:
    print(
        f"{edge['from']} "
        f"--{edge['relationship']}--> "
        f"{edge['to']}"
    )
