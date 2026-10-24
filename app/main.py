from fastapi import FastAPI
from app.models import TicketRequest, TicketAnalysis
from app.retrieval import retrieve
from app.policy import evaluate_action
from app.audit import audit_event

app = FastAPI(
    title="XYZ General Insurance — AI Support Reference API",
    version="0.1.0",
    description="Sanitized local reference scaffold. Uses fictional data and does not call external systems.",
)


def classify(ticket: TicketRequest) -> str:
    text = f"{ticket.subject} {ticket.description} {ticket.error_code or ''}".lower()
    if ticket.error_code or any(term in text for term in ("error code", "http 4", "http 5", "timeout", "failed", "failure")):
        return "api_error"
    if any(term in text for term in ("how do i", "how to", "where can i", "what is the process")):
        return "how_to"
    if any(term in text for term in ("outage", "unavailable", "incident", "not working")):
        return "incident"
    return "unknown"


@app.get("/health")
def health():
    return {"status": "ok", "mode": "local-reference", "external_integrations_enabled": False}


@app.post("/tickets/analyze", response_model=TicketAnalysis)
def analyze_ticket(ticket: TicketRequest):
    category = classify(ticket)
    evidence = retrieve(
        f"{ticket.subject} {ticket.description} {ticket.application} {ticket.error_code or ''}",
        top_k=5,
    )
    if evidence:
        draft = (
            "Draft for L1 review: Based on the available reference material, review the relevant "
            "procedure below and verify the current status in the approved system before responding. "
            "Do not perform a data change based solely on this recommendation."
        )
    else:
        draft = (
            "Draft for L1 review: I could not find sufficiently relevant guidance in the demo knowledge "
            "base. Please validate the issue and route it to the appropriate support team."
        )

    decision = evaluate_action("draft_reply", allowlisted_low_risk=False)
    audit_event("ticket_analyzed", ticket.ticket_id, {"category": category, "evidence_count": len(evidence)})
    return TicketAnalysis(
        ticket_id=ticket.ticket_id,
        category=category,
        summary=ticket.subject.strip(),
        draft_response=draft,
        evidence=evidence,
        requires_human_approval=True,
        proposed_action="draft_only_no_external_action",
        safety_notes=[
            "Synthetic demo data only.",
            "No email is sent and no enterprise API is called.",
            "Human review is required before any response is dispatched.",
            "Never treat model confidence as authorization.",
        ],
        status="draft_for_review",
    )
