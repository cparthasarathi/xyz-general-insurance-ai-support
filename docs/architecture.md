# Architecture and Boundaries

## Local reference mode
- FastAPI validates requests.
- Rule-based demo classification assigns a broad category.
- A lexical retriever searches only fictional Markdown knowledge documents.
- The response is a draft, always requiring review.
- Audit helper emits minimal metadata; this local example does not persist audit events.
- No emails are sent and no enterprise API is invoked.

## AWS target pattern (not implemented in this repository)
- Ingestion: approved S3 source bucket and Bedrock Knowledge Bases data source.
- Embeddings: Amazon Titan Text Embeddings V2, invoked through the configured Knowledge Base ingestion/query workflow.
- Vector store: choose one after evaluation (OpenSearch Serverless, S3 Vectors, or Aurora PostgreSQL/pgvector). They are alternatives, not three mandatory components.
- Agent application: Strands Agents hosted in AgentCore Runtime, if selected; alternatively host agent services on ECS Fargate. Avoid duplicating runtime responsibilities.
- Eventing: SQS for buffering/retries; EventBridge only when decoupled event routing is useful.
- Integrations: Summit ITSM, approved mailbox/email adapter, and allowlisted business APIs.
- Governance: IAM, Secrets Manager, KMS, CloudWatch, CloudTrail, and X-Ray as appropriate.

## Safety boundaries
- The LLM can classify, retrieve, summarize, and draft.
- The LLM cannot grant its own permissions or bypass application policy.
- Data modifications and external actions require explicit human approval by default.
- Validate authorization, ticket state, idempotency, and target-system status outside the model.
- Treat source documents and ticket text as untrusted; retrieved prompt-injection text must not alter system policy.
