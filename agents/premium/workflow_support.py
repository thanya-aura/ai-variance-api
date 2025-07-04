
from typing import List, Dict

def generate_approval_flow(roles: List[str]) -> List[Dict[str, str]]:
    role_map = {
        "initiator": "Editor",
        "approver": "Approver",
        "auditor": "Admin"
    }
    flow = []
    for role in roles:
        mapped_role = role_map.get(role, "Viewer")
        flow.append({
            "role": mapped_role,
            "status": "Pending"
        })
    return flow
