from agents.premium.workflow_support import generate_approval_flow

def test_generate_flow():
    roles = ["initiator", "approver", "auditor"]
    expected_mappings = {
        "initiator": "Editor",
        "approver": "Approver",
        "auditor": "Admin"
    }

    flow = generate_approval_flow(roles)

    assert isinstance(flow, list)
    assert len(flow) == len(roles)

    for i, step in enumerate(flow):
        expected_role = expected_mappings[roles[i]]
        assert "role" in step
        assert "status" in step
        assert step["role"] == expected_role
        assert step["status"] == "Pending"
