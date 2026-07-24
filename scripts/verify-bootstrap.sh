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
)

for required_file in "${required_files[@]}"; do
  if [[ ! -f "$required_file" ]]; then
    echo "Missing required file: $required_file" >&2
    exit 1
  fi
done

sha256sum --check docs/evidence/baselines.sha256

if ! grep -q "live carrier route remains disabled" README.md; then
  echo "README is missing the live-carrier safety boundary." >&2
  exit 1
fi

if ! grep -q "Live carrier credentials" AGENTS.md; then
  echo "AGENTS.md is missing the carrier credential prohibition." >&2
  exit 1
fi

echo "erFam bootstrap verification passed."
