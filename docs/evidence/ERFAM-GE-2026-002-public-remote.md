# Public remote gate evidence

- Evidence ID: `ERFAM-GE-2026-002`
- Repository: `darkest-pearl/erFam`
- Verification date: 2026-07-25
- Candidate baseline commit:
  `aa1206da15ba757e19d841c3ee3c402de0ed9f6a`
- GitHub Actions run:
  `https://github.com/darkest-pearl/erFam/actions/runs/30126974919`
- CI conclusion: `success`
- Independent alpha verdict: `APPROVE`
- Result: `PASS`

Verified controls:

- public visibility was explicitly selected by the owner;
- protected `main`, including administrators, with strict required `verify`
  status;
- two approvals, stale-review dismissal, last-push approval, resolved
  conversations, linear history, and no force pushes or deletion;
- `CODEOWNERS`, squash-only merge, and automatic branch deletion;
- secret scanning, push protection, vulnerability alerts, Dependabot security
  updates, and private vulnerability reporting;
- successful bootstrap workflow on commit `8048342`.

The earlier bootstrap run on `8048342` predates this policy. The candidate
baseline itself passed the strict `verify` workflow on the full SHA recorded
above.

Independent repository scans found no credentials, production phone numbers,
SIM identifiers, call records, recordings, embedded DOCX objects, tracked
changes, macros, or personal document metadata.

Known and accepted limitation: public copies already downloaded cannot be
recalled by a later visibility change.

## Independent alpha verdict

`APPROVE`. A-001 is closed as an explicitly accepted and bounded
public-disclosure risk; A-002 is closed through actionable `SECURITY.md`
guidance and enabled GitHub private vulnerability reporting. Candidate baseline
`aa1206da15ba757e19d841c3ee3c402de0ed9f6a` passed run `30126974919`, and
evidence commit `4b33d8dc2b36ad04be1b7961d9a01352784eb72b` passed run
`30127023027`.

Live GitHub settings independently confirmed administrator-enforced branch
protection, strict `verify`, two approvals, CODEOWNERS review, stale/last-push
controls, resolved conversations, linear history, and force-push/deletion
blocking. TM-11 covers repository-administrator and supply-chain compromise.
ERFAM-WP-2026-001 is complete and the P1 public-baseline gate is closed for
build-track work; L0–L4 remain separate authorization gates.
