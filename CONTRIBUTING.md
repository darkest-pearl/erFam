# Contributing

## Before making a change

1. Read `AGENTS.md` and the relevant approved product documents.
2. Identify the contract, invariant, and acceptance criteria affected.
3. Declare the paths the task is allowed to change.
4. Record unresolved product or architecture ambiguity as
   `DECISION_REQUIRED`.

## Change requirements

- Add or update tests for every behavioral change.
- Include failure, retry, concurrency, and authorization cases where relevant.
- Update versioned contracts before dependent implementations.
- Keep secrets and personal data out of commits, fixtures, logs, and screenshots.
- Do not enable the live carrier route.

## Pull requests

Pull requests must describe the behavior changed, evidence produced, rollback
plan, and any remaining risks. Changes requiring alpha review may not merge
without that review.
