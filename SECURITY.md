# Security Policy

## Scope
This is a sanitized reference project with fictional data. It is not approved for production use without a formal security and architecture review.

## Never commit
- Real customer, policyholder, claimant, employee, vendor, or user data.
- Real tickets, email threads, screenshots, logs, attachments, or exported knowledge-base documents.
- Credentials, API keys, session cookies, bearer tokens, private keys, certificates, account IDs, production URLs, private IPs, or security-group details.
- Internal customer names or information that could re-identify a client even after superficial renaming.

## Required controls before deployment
- Use IAM roles and least privilege; do not embed long-lived AWS credentials.
- Store secrets in AWS Secrets Manager or an approved secret store.
- Encrypt data in transit and at rest; use KMS where applicable.
- Enforce authorization and tenant/access filters before retrieval.
- Require human approval for data changes and external actions unless a documented policy explicitly authorizes a narrow low-risk operation.
- Treat retrieved documents and ticket content as untrusted input; defend against prompt injection.
- Log decision metadata without unnecessarily logging sensitive content.
- Define retention, deletion, audit, incident response, and access-review procedures.
- Run SAST, dependency scanning, secret scanning, and threat modeling.

## Reporting
Do not open a public issue containing sensitive data. Remove the sensitive material from the repository and its history, rotate exposed credentials, and follow the organization's incident-response process.
