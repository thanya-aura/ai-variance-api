
from datetime import datetime
from typing import Any, Dict, List

AUDIT_LOG: List[Dict[str, Any]] = []

def log_field_change(actor: str, field: str, old_value: Any, new_value: Any, reason: str) -> None:
    AUDIT_LOG.append({
        "timestamp": datetime.utcnow().isoformat(),
        "actor": actor,
        "type": "Field Change",
        "details": {
            "field": field,
            "old_value": old_value,
            "new_value": new_value,
            "reason": reason
        }
    })

def get_audit_log() -> List[Dict[str, Any]]:
    return AUDIT_LOG
