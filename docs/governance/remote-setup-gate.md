# Remote repository setup gate

The GitHub remote is not yet available. Before feature branches or parallel
agent pull requests begin, the owner must verify and record:

- the repository is private and owned by `darkest-pearl`;
- `main` is protected from force pushes and deletion;
- changes require pull requests and the quality workflow;
- code-owner review is required for governed paths;
- gate-sensitive changes require two independent approvals;
- dismissal of stale approvals is enabled;
- conversations must be resolved before merge;
- secret scanning and push protection are enabled when available;
- the social-preview image and repository visibility are correct.

Until this gate is evidenced, the local bootstrap commit may be prepared, but
feature implementation must not begin.
