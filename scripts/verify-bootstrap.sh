#!/usr/bin/env bash
set -euo pipefail

repository_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repository_root"

required_files=(
  "README.md"
  "AGENTS.md"
  "SECURITY.md"
  "CONTRIBUTING.md"
  "docs/product/erFam_PRD_v0.3.docx"
  "docs/product/erFam_Product_Design_v0.2.docx"
  "docs/product/erFam_Implementation_Plan_v0.1.docx"
  "docs/branding/erFam_social_preview.png"
  "docs/evidence/baselines.sha256"
  "docs/evidence/ERFAM-AR-2026-001-bootstrap.md"
  "docs/evidence/ERFAM-GE-2026-002-public-remote.md"
  "docs/governance/public-repository-policy.md"
  "docs/security/threat-model.md"
  "contracts/governance-policy.json"
  "docs/templates/agent-work-package.md"
  "docs/templates/alpha-verdict.md"
  "docs/templates/architecture-decision.md"
  "docs/templates/contract-change.md"
  "docs/templates/gate-evidence.md"
)

for required_file in "${required_files[@]}"; do
  if [[ ! -f "$required_file" ]]; then
    echo "Missing required file: $required_file" >&2
    exit 1
  fi
done

declare -A expected_hashes=(
  ["docs/product/erFam_PRD_v0.3.docx"]="80cef573100cecde591109a36fdae93f357b141ae7f58a91e6208063750ac07c"
  ["docs/product/erFam_Product_Design_v0.2.docx"]="534388eaf1a175198d04ae36df3829b96dc7042d4ee4ef6ca3d3e1086516461b"
  ["docs/product/erFam_Implementation_Plan_v0.1.docx"]="834ddd6779669ef087209a68a6fccb55acc9367398aba52a9b8b571d1b078efd"
  ["docs/branding/erFam_social_preview.png"]="a242cc7741aef07c74fc6d51429a3c0d94b5f43379029c6437fa818b10a21040"
)

for baseline_path in "${!expected_hashes[@]}"; do
  actual_hash="$(sha256sum "$baseline_path" | cut -d ' ' -f 1)"
  if [[ "$actual_hash" != "${expected_hashes[$baseline_path]}" ]]; then
    echo "Approved baseline changed: $baseline_path" >&2
    exit 1
  fi
done

sha256sum --check docs/evidence/baselines.sha256

python3 - <<'PY'
import json
from pathlib import Path

policy = json.loads(Path("contracts/governance-policy.json").read_text())

assert policy["schema_version"] == 1
assert policy["build_track"]["allowed_routes"] == [
    "demo",
    "simulated",
    "isolated",
]
assert policy["build_track"]["live_credentials_allowed"] is False
assert policy["build_track"]["real_outbound_traffic_allowed"] is False
assert policy["live_track"]["default_enabled"] is False
assert policy["live_track"]["unrestricted_production_requires"] == "L4"
assert [stage["id"] for stage in policy["live_track"]["stages"]] == [
    "L0",
    "L1",
    "L2",
    "L3",
    "L4",
]
assert all(stage["prior_approval_required"] for stage in policy["live_track"]["stages"])
assert all(stage["evidence_required"] for stage in policy["live_track"]["stages"])
assert all(stage["rollback_required"] for stage in policy["live_track"]["stages"])

reveal = policy["privacy"]["administrator_destination_reveal"]
assert reveal == {
    "attributable_audit_event_required": True,
    "fresh_step_up_required": True,
    "mandatory_reason_required": True,
    "masked_by_default": True,
}

assert policy["semantics"]["duration"] == {
    "allow_negative": False,
    "storage": "integer_seconds",
}
assert policy["semantics"]["money"] == {
    "allow_floating_point": False,
    "storage": "integer_fils",
}
PY

./scripts/verify-public-safety.sh

echo "erFam bootstrap verification passed."
