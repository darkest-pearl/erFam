# Evidence

Store non-sensitive review reports, test summaries, performance baselines,
activation-gate evidence, and rollback results here. Never store production
phone numbers, credentials, private keys, or recordings.

Use `docs/templates/gate-evidence.md` and `docs/templates/alpha-verdict.md`.
Changes to approved product baselines require explicit owner approval,
independent alpha review, and a recorded reason. GitHub branch protection must
require code-owner review for the baseline files once the remote exists.
