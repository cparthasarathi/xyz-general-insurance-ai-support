# Synthetic API Error Catalog

## DEMO-HTTP-504: Timeout
Meaning: A downstream service did not respond within the configured timeout.
Initial checks: Confirm service health in the approved monitoring dashboard and check whether the request outcome is known.
Recovery: Follow the approved retry policy only after checking idempotency and current transaction status.
Restrictions: Do not blindly retry a transaction with an uncertain outcome. Escalate if status cannot be verified.

## DEMO-AUTH-401: Authentication Failure
Meaning: The synthetic service rejected the request due to missing or invalid authorization.
Initial checks: Confirm the service identity and secret reference through the approved secret-management workflow.
Recovery: Route credential rotation to the authorized operations process.
Restrictions: Never put credentials or tokens into tickets, prompts, source code, or logs.
