# Public remote gate evidence

- Evidence ID: `ERFAM-GE-2026-002`
- Repository: `darkest-pearl/erFam`
- Verification date: 2026-07-25
- Candidate baseline commit:
  `aa1206da15ba757e19d841c3ee3c402de0ed9f6a`
- GitHub Actions run:
  `https://github.com/darkest-pearl/erFam/actions/runs/30126974919`
- CI conclusion: `success`
- Independent alpha verdict: `BLOCK` pending corrections and exact-SHA CI
- Result: `PENDING`

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
