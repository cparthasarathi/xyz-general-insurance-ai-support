"""Conservative policy gate. Model output or confidence never grants authorization."""
from dataclasses import dataclass


@dataclass(frozen=True)
class PolicyDecision:
    requires_human_approval: bool
    allowed_to_execute: bool
    reason: str


def evaluate_action(action_type: str, *, allowlisted_low_risk: bool = False) -> PolicyDecision:
    normalized = action_type.strip().lower()
    # This reference project does not execute any external actions.
    if normalized in {"read_only_lookup", "draft_reply"} and allowlisted_low_risk:
        return PolicyDecision(
            requires_human_approval=False,
            allowed_to_execute=False,
            reason="Demo mode: no external execution is wired. Production allowlisting is required.",
        )
    return PolicyDecision(
        requires_human_approval=True,
        allowed_to_execute=False,
        reason="External actions, writes, and unclassified operations require human approval.",
    )
