"""Minimal structured audit event helper; production should use approved durable logging."""
from datetime import datetime, timezone


def audit_event(event_type: str, ticket_id: str, details: dict | None = None) -> dict:
    # Avoid putting full ticket text, credentials, or personal data into audit details.
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event_type": event_type,
        "ticket_id": ticket_id,
        "details": details or {},
    }
