#!/usr/bin/env bash
set -euo pipefail

repository_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repository_root"

failures=0

report_match() {
  local label="$1"
  local pattern="$2"
  shift 2

  if git grep -nEI "$pattern" -- "$@" >"/tmp/erfam-public-safety-match" 2>/dev/null; then
    echo "Public-safety check failed: $label" >&2
    sed -n '1,20p' /tmp/erfam-public-safety-match >&2
    failures=$((failures + 1))
  fi
}

report_match \
  "private key material" \
  '-----BEGIN (RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----' \
  .

report_match \
  "high-confidence credential assignment" \
  '(api[_-]?key|client[_-]?secret|access[_-]?token|refresh[_-]?token|password)[[:space:]]*[:=][[:space:]]*["'\"'][A-Za-z0-9_./+=-]{12,}' \
  ':!docs/product/**' ':!scripts/verify-public-safety.sh'

report_match \
  "GitHub token" \
  '(gh[opurs]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,})' \
  .

report_match \
  "cloud access key" \
  '(AKIA|ASIA)[A-Z0-9]{16}' \
  .

if git ls-files | grep -E '(^|/)(\.env($|\.)|local\.properties$|.*\.(jks|keystore|pem|key)$)' >/tmp/erfam-public-safety-files; then
  echo "Public-safety check failed: tracked secret-bearing filename" >&2
  sed -n '1,20p' /tmp/erfam-public-safety-files >&2
  failures=$((failures + 1))
fi

if git grep -nE 'REAL_LIVE|realAdapterEnabled[[:space:]]*[:=][[:space:]]*true' -- \
  ':!docs/product/**' ':!docs/security/**' ':!scripts/verify-public-safety.sh' \
  >/tmp/erfam-live-route-match 2>/dev/null; then
  echo "Public-safety check failed: build-track live-route token" >&2
  sed -n '1,20p' /tmp/erfam-live-route-match >&2
  failures=$((failures + 1))
fi

if (( failures > 0 )); then
  exit 1
fi

echo "erFam public-safety verification passed."
