# Security Policy

erFam handles identity, calling metadata, and encrypted destination data.
Security and privacy defects must not be discussed in public issues.

## Reporting

Use
[GitHub private vulnerability reporting](https://github.com/darkest-pearl/erFam/security/advisories/new)
to report a suspected vulnerability. Include the affected version, impact,
reproduction steps using synthetic data, and any suggested mitigation.

Do not include production phone numbers, credentials, SIM identifiers, call
recordings, plaintext destinations, or other personal data in a report.

## Sensitive data rules

- Never commit credentials, tokens, SIM identifiers, private keys, production
  phone numbers, raw call recordings, or unmasked call-detail records.
- Use synthetic fixtures in every automated test.
- Keep recording on the caller's device only.
- Treat carrier activation as a privileged, audited, fail-closed operation.
- Do not add third-party analytics to authentication, calling, destination
  reveal, recovery, or audit views.
