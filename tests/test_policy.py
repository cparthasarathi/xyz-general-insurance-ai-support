from app.policy import evaluate_action


def test_external_action_requires_approval():
    result = evaluate_action("update_policy_record", allowlisted_low_risk=True)
    assert result.requires_human_approval is True
    assert result.allowed_to_execute is False


def test_demo_does_not_execute_even_allowlisted_action():
    result = evaluate_action("read_only_lookup", allowlisted_low_risk=True)
    assert result.allowed_to_execute is False
