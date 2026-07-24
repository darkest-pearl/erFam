# erFam Agent Operating Contract

This file applies to every human and automated contributor in this repository.

## Authority

The following documents are authoritative, in order:

1. `docs/product/erFam_PRD_v0.3.docx`
2. `docs/product/erFam_Product_Design_v0.2.docx`
3. `docs/product/erFam_Implementation_Plan_v0.1.docx`
4. Accepted architecture decision records in `docs/adr`

If implementation is ambiguous or conflicts with these sources, stop and
record `DECISION_REQUIRED`; do not silently invent behavior.

## Required engineering behavior

- Keep one authoritative state reducer, allocation ledger, and destination
  parser. Clients render server truth and do not recreate business rules.
- Model time as non-negative integer seconds and money as integer fils.
- Reject invalid state transitions explicitly. Never clamp, underflow, or
  reinterpret negative availability as callable time.
- Make retries idempotent and externally visible actions traceable by
  correlation ID.
- Preserve deterministic behavior under concurrency, retries, reconnects, and
  delayed events.
- Use versioned contracts and additive compatibility unless a reviewed
  migration says otherwise.
- Fail closed when identity, policy, quota, destination, gateway health, or
  authorization state is unknown.

## Carrier safety boundary

- B1–B6 use demo, simulated, or isolated routes only.
- The real line driver must use the reviewed SIP/PJSIP interface through
  Asterisk and the `GatewayTelemetryPlugin` boundary.
- Unsupported gateway telemetry is represented as `UNKNOWN` or `UNSUPPORTED`;
  it is never fabricated.
- Live carrier credentials, SIM routing, and real outbound traffic are
  prohibited on the build track. The live track may use only the minimum
  controlled traffic explicitly authorized by its current gate: L0 carrier
  authorization, L1 isolated hardware validation, L2 scoped verification
  calls, L3 limited alpha, and L4 production activation.
- Each live-track stage requires prior approval, recorded scope, evidence, and a
  tested rollback. Unrestricted production traffic is prohibited before L4.
- The live route remains disabled after implementation unless an authorized,
  audited activation changes it within the approved stage.

## Privacy and security

- Never log plaintext destination numbers, DTMF, OTPs, access tokens,
  credentials, encryption keys, or raw media.
- Encrypt full destination numbers at rest and mask them by default. A caller
  may reveal their own destination. An authorized administrator reveal requires
  fresh step-up authentication, a mandatory reason, and an attributable audit
  event.
- Call recording is opt-in, locally stored on the member device, and unavailable
  to administrators or cloud services.
- Default destination retention is four months and must be configurable.

## Review ownership

Alpha review is required for changes to:

- identity, device binding, and recovery;
- state machines, allocation, ledgers, and fairness;
- cryptography, retention, and privacy;
- PBX, media, line drivers, and carrier activation;
- migrations, deployment, and security controls.

Each task must name its allowed paths. Do not modify another task's owned paths
without coordination. Prefer small, reviewable commits with tests and evidence.

## Streamed multi-agent delivery

- The lead integrator decomposes work into bounded tasks with acceptance
  criteria, dependencies, and explicit path ownership.
- Specialists stream material findings, blockers, contract changes, and
  verification results to the lead while they work.
- The lead integrates specialist output and remains accountable for repository-
  wide coherence; agent output is never merged blindly.
- A `gpt-5.6-sol` alpha reviewer independently reviews cross-component
  semantics and gate-sensitive changes.
- An alpha reviewer may not approve work it authored or materially implemented.
- Simpler, isolated tasks may use a more economical agent only when their
  outputs are deterministically verifiable.
- Parallel work must not overlap writable paths unless the lead explicitly
  coordinates the overlap.
- Unpredictable or ambiguous behavior is a blocker: stop, preserve evidence,
  and raise `DECISION_REQUIRED`.
