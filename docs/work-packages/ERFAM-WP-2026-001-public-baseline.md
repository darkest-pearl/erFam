# ERFAM-WP-2026-001 — Public governance and security baseline

- Status: complete
- Owner: lead integrator
- Reviewer: security architecture agents
- Alpha reviewer: `gpt-5.6-sol`
- Dependencies: repository bootstrap
- Allowed paths: `SECURITY.md`, `README.md`, `docs/governance/**`,
  `docs/security/**`, `docs/evidence/**`, `.github/**`
- Prohibited paths: product source code

## Outcome

Permit implementation in the intentionally public repository without allowing
secrets, personal data, or live-carrier material into the build track.

## Acceptance criteria

- Remote protections and security features are verified.
- Private vulnerability reporting is enabled.
- Public exposure is explicitly accepted and bounded.
- Architecture threats and deterministic verification obligations are recorded.

## Carrier stage

Build track B1–B6 only. Real outbound traffic and credentials are prohibited.

## Evidence

See `docs/evidence/ERFAM-GE-2026-002-public-remote.md`.
