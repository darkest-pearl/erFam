# erFam build-track threat model

Status: accepted build-track baseline  
Scope: Android member app, administrator web app, control service, media
control, home-edge service, virtual gateway, and the locked real adapter

## Assets

- member and administrator identities;
- device bindings, recovery state, sessions, and step-up assertions;
- allocation requests, integer-second balances, reservations, and ledger;
- encrypted destinations and masked call history;
- call and gateway state, correlation IDs, audit events, and safe telemetry;
- live-route activation state and carrier-adapter configuration.

## Trust boundaries

1. Android or browser to the cloud control boundary.
2. Administrator browser to privileged control and reveal operations.
3. Control service to media-control and PBX/event sources.
4. Cloud to the home-edge WireGuard and workload-identity boundary.
5. Home-edge to virtual or real carrier adapters.
6. Local Android recording storage to the operating-system backup/export
   boundary.

## Required mitigations

| ID | Threat | Required mitigation | Verification |
| --- | --- | --- | --- |
| TM-01 | Public repository exposes private data or secrets | Synthetic fixtures, secret scanning, push protection, publication policy | repository scan and CI |
| TM-02 | Browser session or cross-site request theft | HttpOnly, Secure, SameSite cookies; CSRF and Origin checks; rotation; `no-store`; restrictive CSP and Referrer-Policy | web security tests |
| TM-03 | Forged or replayed PBX/gateway events corrupt call truth | Authenticated workload channel, correlation and event IDs, monotonic sequence/version, timestamp window, idempotent reducer | contract and replay tests |
| TM-04 | Recovery flow hijacks a member account | Pending recovery, administrator confirmation, cooldown, old-session revocation, member notification, attributable audit | recovery integration tests |
| TM-05 | Destination reveal leaks through cache, URL, logs, or broad authorization | Resource-scoped short-lived reveal, fresh step-up, reason, audit, no caching, no URL/storage persistence | reveal and log-safety tests |
| TM-06 | Digital twin reaches a real carrier or external destination | No carrier credentials, fake command recorder, allowlisted synthetic `+291` fixtures, hard network egress isolation, negative route tests | simulator and infrastructure tests |
| TM-07 | Local call recording reaches administrator, cloud, backup, or another app | Feature gated and off by default, app-private encrypted storage, backup excluded, no exported provider or upload API | Android manifest/storage tests |
| TM-08 | Concurrent requests spend time twice or show negative callable time | One authoritative integer-second ledger, atomic reservation, idempotency key, compensating entry, non-negative invariant | concurrency/property tests |
| TM-09 | Delayed or duplicate events regress a terminal call or free an uncertain line | One reducer; ignore duplicate/stale versions; fail closed; reconciliation holds uncertain line | state-machine model tests |
| TM-10 | Real adapter is enabled as an ordinary feature | Compile and test the adapter, ship `LOCKED`/`REAL_DRY_RUN`, omit credentials/routes, require separate audited live gate | configuration and negative tests |
| TM-11 | Repository administrator or compromised automation bypasses review and injects unsafe source or dependencies | Enforce branch protection for administrators, strict required checks, two independent approvals, CODEOWNERS, least-privilege Actions permissions, pinned actions, phishing-resistant MFA, secret/push protection, and repository audit review | GitHub settings evidence and exact-SHA CI |

## Browser security baseline

Sensitive responses use `Cache-Control: no-store`, a restrictive
`Content-Security-Policy`, `Referrer-Policy: no-referrer`, and
`X-Content-Type-Options: nosniff`. Session tokens are never written to URLs,
local storage, or application logs. Sensitive pages have no third-party
analytics.

## Event authenticity baseline

Every gateway event includes a unique event ID, call correlation ID, aggregate
version, source identity, and occurred-at timestamp. Services reject unknown
sources, invalid signatures or workload credentials, events outside the
configured replay window, and transitions rejected by the canonical reducer.

## Carrier boundary

The virtual adapter is the only routable build-track adapter. The real adapter
is implemented against the reviewed SIP/PJSIP boundary, but remains locked and
dry-run-only with no carrier credentials or real outbound route. Unsupported
telemetry is represented as `UNKNOWN` or `UNSUPPORTED`, never invented.

## Residual risks

- Public architectural disclosure cannot be recalled from existing clones.
- A build-track simulator cannot prove carrier interoperability, RF behavior,
  audio quality, or carrier policy compliance.
- L0 carrier authorization and later live-track gates remain separate,
  explicitly approved activities.
