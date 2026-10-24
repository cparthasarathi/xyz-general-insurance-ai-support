# Chunking Strategy

## Goal
Retrieve concise, authoritative evidence for L1 support without separating procedures from prerequisites, warnings, or verification steps.

## By source type

### SOPs and runbooks
- Preserve section headings, numbered steps, prerequisites, warnings, rollback, and verification.
- Where supported and evaluation proves useful, use hierarchical parent/child chunking: parent context around 1,000–1,500 tokens and child chunks around 250–400 tokens as an initial experiment.
- Otherwise use structure-aware fixed-size chunks. Start around 500 tokens with 50–75 tokens of overlap as a test hypothesis, not a hard rule.
- Avoid splitting a step from its required warning or prerequisite.

### Historical tickets
- Keep one incident per logical chunk where possible.
- Include incident ID, application, symptoms, error code, root cause, resolution, verification, resolution status, and timestamps when appropriate.
- For long histories, split by troubleshooting stage while preserving incident ID and parent reference in metadata.
- Do not mix unrelated incidents in the same chunk.

### API documentation and error catalogs
- Keep one API operation or error definition together with request/response schema, error meaning, remediation, and authorization restrictions.
- Preserve exact error codes, endpoint names, and version metadata.

### FAQs
- Keep each question with its full answer. Use no chunking only for small, self-contained files when supported by the chosen ingestion configuration.

## Metadata schema
Recommended fields:
- `document_id`
- `document_type` (`sop`, `runbook`, `incident`, `api`, `faq`)
- `application`
- `incident_category`
- `error_code`
- `api_name`
- `version`
- `effective_date`
- `access_classification`
- `source_status` (`approved`, `draft`, `retired`)

Apply authorization/access filters before returning retrieved passages. Metadata is not a substitute for access control.

## Evaluation
Build 50–100 sanitized test questions spanning exact error-code lookup, how-to instructions, multi-step troubleshooting, exception handling, and ambiguous requests. Compare chunk configurations using recall@k, evidence completeness, answer faithfulness, latency, and cost.

For S3 Vectors, verify supported chunking options in the selected Bedrock Knowledge Bases configuration. Do not assume all vector stores expose identical chunking features.
