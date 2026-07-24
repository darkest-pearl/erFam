# Security Policy

erFam handles identity, calling metadata, and encrypted destination data.
Security and privacy defects should not be discussed in public issues.

## Reporting

For this private bootstrap, report suspected vulnerabilities directly to the
repository owner through a private channel. A dedicated security contact will
be documented before external testing.

## Sensitive data rules

- Never commit credentials, tokens, SIM identifiers, private keys, production
  phone numbers, raw call recordings, or unmasked call-detail records.
- Use synthetic fixtures in every automated test.
- Keep recording on the caller's device only.
- Treat carrier activation as a privileged, audited, fail-closed operation.
