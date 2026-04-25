#!/data/data/com.termux/files/usr/bin/bash

FILE="governance/execution/execution_time_governance_spec.md"

fail() {
  echo "FAIL: $1"
  exit 1
}

[ -f "$FILE" ] || fail "Spec file not found"

grep -q "Decision Boundary" "$FILE" || fail "Missing Decision Boundary"
grep -q "Escalation" "$FILE" || fail "Missing Escalation"
grep -q "Stop Authority" "$FILE" || fail "Missing Stop Authority"
grep -q "Accountability" "$FILE" || fail "Missing Accountability"
grep -q "Governance Telemetry" "$FILE" || fail "Missing Governance Telemetry"

echo "PASS: Execution-Time Governance Spec is valid"
exit 0
