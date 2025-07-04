from agents.premium.audit_log import log_field_change, get_audit_log

def test_log_field_change_entry():
    # Clear the log before testing
    get_audit_log().clear()

    # Log a sample field change
    log_field_change(
        actor="controller",
        field="Cost",
        old_value=5000,
        new_value=7000,
        reason="Supplier price adjustment"
    )

    # Retrieve and validate the log entry
    log = get_audit_log()
    assert len(log) == 1
    entry = log[0]
    assert entry["actor"] == "controller"
    assert entry["type"] == "Field Change"
    assert entry["details"]["field"] == "Cost"
    assert entry["details"]["old_value"] == 5000
    assert entry["details"]["new_value"] == 7000
    assert entry["details"]["reason"] == "Supplier price adjustment"
    assert "timestamp" in entry
