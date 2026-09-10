#!/usr/bin/env python3
"""Scan source without interpreting Git errors as an empty, safe repository."""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECRET_NAME = re.compile(r"(^|/)(\.env($|\.)|local\.properties$|.*\.(jks|keystore|pem|key)$)")
PATTERNS = {
    "private key material": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    "credential assignment": re.compile(r'''(?:api[_-]?key|client[_-]?secret|access[_-]?token|refresh[_-]?token|password)\s*[:=]\s*["'][A-Za-z0-9_./+=-]{12,}''', re.I),
    "GitHub token": re.compile(r"(?:gh[opurs]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,})"),
    "cloud access key": re.compile(r"(?:AKIA|ASIA)[A-Z0-9]{16}"),
}

def source_files(root):
    # --others includes not-yet-committed source; ignored build caches are excluded.
    result = subprocess.run(["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
                            cwd=root, capture_output=True, check=True)
    return sorted(set(result.stdout.decode("utf-8").split("\0")) - {""})

def scan(root):
    findings = []
    for name in source_files(root):
        if SECRET_NAME.search(name):
            findings.append((name, "secret-bearing filename"))
        path = root / name
        if not path.is_file():
            raise ValueError("indexed source is missing or not a regular file")
        data = path.read_bytes()
        if b"\0" in data:
            continue
        content = data.decode("utf-8", errors="replace")
        for label, pattern in PATTERNS.items():
            if label == "credential assignment" and (name.startswith("docs/product/") or name in {
                "scripts/verify-public-safety.sh", "scripts/verify-public-safety.py"}):
                continue
            if pattern.search(content):
                findings.append((name, label))
        if not (name.startswith(("docs/product/", "docs/security/")) or name in {
            "scripts/verify-public-safety.sh", "scripts/verify-public-safety.py"}):
            if re.search(r"REAL_LIVE|realAdapterEnabled\s*[:=]\s*true", content):
                findings.append((name, "build-track live-route token"))
    return findings

def main():
    try:
        findings = scan(ROOT)
    except (OSError, ValueError, subprocess.SubprocessError):
        # Never print potentially sensitive Git diagnostics or matched source values.
        print("Public-safety inspection failed; source could not be completely inspected.", file=sys.stderr)
        return 2
    for name, label in findings:
        print(f"Public-safety check failed: {label} in {name}", file=sys.stderr)
    if findings:
        return 1
    print("erFam public-safety verification passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
