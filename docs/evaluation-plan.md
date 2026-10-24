# Evaluation Plan

## Dataset
Create 50–100 sanitized, synthetic support questions:
- 20 SOP/how-to questions
- 15 exact error-code and API questions
- 15 historical incident/root-cause questions
- 10 multi-step troubleshooting questions
- 10 ambiguous or out-of-scope requests

## Metrics
- Retrieval recall@3 and recall@5
- Evidence completeness and source relevance
- Answer faithfulness and unsupported-claim rate
- Correct escalation / human-approval rate
- p50/p95 latency and cost per analyzed ticket
- API action authorization and idempotency tests (when integrations are added)

## Acceptance gates
Set thresholds with the product owner after a baseline run. Never infer acceptance from a single aggregate accuracy score. Include adversarial prompt-injection, authorization, malformed input, and unavailable-dependency cases.
