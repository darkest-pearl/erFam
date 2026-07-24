# erFam

erFam is a private, configurable family-calling platform designed for a small
trusted group. The first release targets Android members, a responsive web
admin console, cloud control services, and one controlled home-edge gateway.

## Current status

This repository is in **B1 — repository and governance bootstrap**. Product
implementation is intentionally locked until the approved requirements,
architecture, semantic catalogue, and security boundaries are represented as
testable contracts.

The real SIM/PSTN adapter is a required product component, not an abandoned
prototype. It must be implemented and tested against a simulated or isolated
environment. Its live carrier route remains disabled by default and must not
carry real traffic until the documented authorization and activation gates are
satisfied.

## Repository layout

| Path | Purpose |
| --- | --- |
| `apps/android` | Android member application |
| `apps/admin` | Responsive administrator web application |
| `services/control` | Identity, policy, allocation, ledger, and call control |
| `services/media-control` | Session and media orchestration |
| `services/home-edge` | Controlled gateway and carrier-adapter runtime |
| `contracts` | Versioned API, event, state, and error contracts |
| `infra` | Cloud and edge infrastructure definitions |
| `tests` | Cross-component contract, integration, and system tests |
| `docs/product` | Approved PRD, product design, and implementation plan |
| `docs/adr` | Architecture decision records |
| `docs/evidence` | Review, test, and activation evidence |
| `docs/runbooks` | Operational and recovery procedures |

## Non-negotiable invariants

- Time is stored and calculated as non-negative integer seconds.
- Money is stored and calculated as integer fils; floating-point money is
  prohibited.
- A displayed balance can never imply callable time below zero.
- Allocation and ledger changes are atomic, idempotent, auditable, and
  reversible through compensating entries.
- Full destination numbers are encrypted at rest and masked by default. A
  caller may reveal their own number; an authorized administrator needs fresh
  step-up authentication, a mandatory reason, and an attributable audit event.
- DTMF, OTPs, access tokens, credentials, raw media, and plaintext destination
  numbers never enter logs or telemetry.
- The demo route is the default. Live carrier activation is a separate,
  fail-closed operational decision.
- Build-track work uses demo, simulated, or isolated routes. Any controlled
  live-track test requires the prior gate's explicit approval and recorded
  scope; unrestricted production traffic requires L4 approval.

## Approved source documents

- `docs/product/erFam_PRD_v0.3.docx`
- `docs/product/erFam_Product_Design_v0.2.docx`
- `docs/product/erFam_Implementation_Plan_v0.1.docx`

Run `scripts/verify-bootstrap.sh` to validate the bootstrap structure and the
approved-document checksums.
