#!/data/data/com.termux/files/usr/bin/bash

echo "{
  \"event\": \"$1\",
  \"actor\": \"amypbui\",
  \"rule_checked\": \"$2\",
  \"action\": \"$3\",
  \"result\": \"$4\",
  \"timestamp\": \"$(date -u +"%Y-%m-%dT%H:%M:%SZ")\"
}" >> GOVERNANCE/telemetry.jsonl
