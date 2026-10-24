from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_discloses_demo_mode():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["external_integrations_enabled"] is False


def test_analyze_returns_draft_and_requires_approval():
    response = client.post("/tickets/analyze", json={
        "ticket_id": "DEMO-1001",
        "subject": "Payment status inquiry",
        "description": "How do I check whether a payment request completed?",
        "application": "PolicyAdmin",
    })
    assert response.status_code == 200
    data = response.json()
    assert data["requires_human_approval"] is True
    assert data["status"] == "draft_for_review"
    assert data["proposed_action"] == "draft_only_no_external_action"
    assert data["safety_notes"]
