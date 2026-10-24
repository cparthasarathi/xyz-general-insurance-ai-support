from typing import Literal
from pydantic import BaseModel, Field, field_validator


class TicketRequest(BaseModel):
    ticket_id: str = Field(min_length=3, max_length=40, pattern=r"^[A-Za-z0-9_-]+$")
    subject: str = Field(min_length=3, max_length=240)
    description: str = Field(min_length=5, max_length=8000)
    application: str = Field(min_length=2, max_length=80)
    error_code: str | None = Field(default=None, max_length=80)

    @field_validator("subject", "description", "application")
    @classmethod
    def trim_text(cls, value: str) -> str:
        return value.strip()


class Evidence(BaseModel):
    document_id: str
    title: str
    excerpt: str
    source_type: str
    relevance_score: float


class TicketAnalysis(BaseModel):
    ticket_id: str
    category: Literal["how_to", "incident", "api_error", "unknown"]
    summary: str
    draft_response: str
    evidence: list[Evidence]
    requires_human_approval: bool
    proposed_action: str
    safety_notes: list[str]
    status: Literal["draft_for_review"] = "draft_for_review"
