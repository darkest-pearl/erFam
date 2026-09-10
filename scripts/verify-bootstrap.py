#!/usr/bin/env python3
"""Portable baseline verifier; approved hashes are independent of manifest contents."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "docs/product/erFam_PRD_v0.3.docx": "80cef573100cecde591109a36fdae93f357b141ae7f58a91e6208063750ac07c",
    "docs/product/erFam_Product_Design_v0.2.docx": "534388eaf1a175198d04ae36df3829b96dc7042d4ee4ef6ca3d3e1086516461b",
    "docs/product/erFam_Implementation_Plan_v0.1.docx": "834ddd6779669ef087209a68a6fccb55acc9367398aba52a9b8b571d1b078efd",
    "docs/branding/erFam_social_preview.png": "a242cc7741aef07c74fc6d51429a3c0d94b5f43379029c6437fa818b10a21040",
}
REQUIRED = ["README.md", "AGENTS.md", "SECURITY.md", "CONTRIBUTING.md",
    "docs/evidence/baselines.sha256", "docs/evidence/ERFAM-AR-2026-001-bootstrap.md",
    "contracts/governance-policy.json", "docs/templates/agent-work-package.md",
    "docs/templates/alpha-verdict.md", "docs/templates/architecture-decision.md",
    "docs/templates/contract-change.md", "docs/templates/gate-evidence.md",
    "docs/governance/public-repository-policy.md", "docs/security/threat-model.md"]

def require(value, message):
    if not value:
        raise ValueError(message)

def verify(root):
    for name in REQUIRED:
        require((root / name).is_file(), "required baseline missing")
    for name, expected in EXPECTED.items():
        require(hashlib.sha256((root / name).read_bytes()).hexdigest() == expected, "approved baseline changed")
    manifest = {}
    for line in (root / "docs/evidence/baselines.sha256").read_text().splitlines():
        digest, name = line.split(maxsplit=1)
        require(name not in manifest, "duplicate baseline manifest entry")
        manifest[name] = digest
    require(manifest == EXPECTED, "baseline manifest differs from approved hashes")
    policy = json.loads((root / "contracts/governance-policy.json").read_text())
    require(policy["schema_version"] == 1, "governance version")
    require(policy["build_track"] == {"allowed_routes": ["demo", "simulated", "isolated"],
        "live_credentials_allowed": False, "real_outbound_traffic_allowed": False}, "build boundary")
    live = policy["live_track"]
    require(live["default_enabled"] is False and live["unrestricted_production_requires"] == "L4", "live boundary")
    require([s["id"] for s in live["stages"]] == ["L0", "L1", "L2", "L3", "L4"], "live stages")
    require(all(s[k] is True for s in live["stages"] for k in
        ("prior_approval_required", "evidence_required", "rollback_required")), "live evidence")
    require(policy["privacy"]["administrator_destination_reveal"] == {
        "attributable_audit_event_required": True, "fresh_step_up_required": True,
        "mandatory_reason_required": True, "masked_by_default": True}, "reveal boundary")
    require(policy["semantics"] == {"duration": {"allow_negative": False, "storage": "integer_seconds"},
        "money": {"allow_floating_point": False, "storage": "integer_fils"}}, "numeric semantics")

if __name__ == "__main__":
    try:
        verify(ROOT)
        subprocess.run([sys.executable, str(ROOT / "scripts/verify-public-safety.py")], check=True)
    except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as error:
        print(f"Bootstrap verification failed ({type(error).__name__}).", file=sys.stderr)
        sys.exit(1)
    print("erFam bootstrap verification passed.")
