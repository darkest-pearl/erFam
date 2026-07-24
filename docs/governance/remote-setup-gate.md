# Remote repository setup gate

Status: **PENDING EXACT-SHA CI AND ALPHA VERDICT**

Verified on 2026-07-25 against
[`darkest-pearl/erFam`](https://github.com/darkest-pearl/erFam).

- Repository visibility is public by the owner's explicit decision.
- Protected `main`, including administrators, prevents force pushes and
  deletion and requires linear history.
- Pull requests, including administrator changes, require the `verify` check,
  resolved conversations, dismissal
  of stale approvals, approval of the most recent push, and two approvals.
- Governed paths use `CODEOWNERS`.
- Secret scanning, push protection, Dependabot security updates, vulnerability
  alerts, and private vulnerability reporting are enabled.
- Squash is the only enabled merge strategy; merged branches are deleted.
- The social preview and public-disclosure policy are recorded.

No administrator bypass is configured. Two independent GitHub approvals are
therefore required before merge; agent alpha verdicts provide additional
engineering evidence but do not impersonate GitHub reviewers.

The public-repository exposure and its limitations are accepted in
`docs/governance/public-repository-policy.md`.

This gate closes only after these files are committed, `verify` succeeds on
that exact SHA, and the independent alpha reviewer approves the evidence.
