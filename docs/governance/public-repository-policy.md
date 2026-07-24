# Public repository policy

## Owner decision

The repository owner explicitly chose public visibility on 2026-07-25 to allow
the implementation environment to clone and collaborate without a private
repository access blocker.

Public visibility means product documents, architecture, use cases, supported
destination policy, and security design are available to anyone. A later
visibility change cannot recall copies already cloned or downloaded.

## Accepted public material

- synthetic examples and test identities;
- architecture and interface contracts;
- the virtual gateway and deterministic fault model;
- product requirements and user-interface concepts;
- evidence that contains no secrets or personal data.

## Prohibited public material

- credentials, tokens, private keys, carrier account data, or SIM identifiers;
- real phone numbers, call-detail records, recordings, or contact lists;
- production IP addresses, VPN configuration, or gateway management secrets;
- vulnerability details before a fix or coordinated disclosure;
- live carrier activation evidence containing restricted information.

## Required controls

- Use private vulnerability reporting for security reports.
- Run secret scanning and push protection.
- Keep fixtures synthetic and visibly marked as such.
- Treat logs, screenshots, recordings, exports, and build artifacts as
  potentially sensitive before publication.
- Keep real carrier traffic and credentials absent from the build track.
- Re-review this policy before any L0–L4 live-track gate.

Owner acceptance: `darkest-pearl`  
Decision date: 2026-07-25  
Review trigger: before external user testing or any live-track activity
