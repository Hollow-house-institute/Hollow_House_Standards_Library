import json
import sys

with open("glossary.json") as f:
    data = json.load(f)

if "terms" not in data:
    print("FAIL: glossary missing 'terms'")
    sys.exit(1)

for term in data["terms"]:
    if "term" not in term or "definition" not in term:
        print("FAIL: invalid term structure")
        sys.exit(1)

print("PASS: glossary structure valid")
