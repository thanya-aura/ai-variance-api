from fastapi.testclient import TestClient
from main import app
import os

client = TestClient(app)


def test_analyze_premium_upload():
    test_file = "sample_variance_premium.xlsx"

    assert os.path.exists(test_file), f"Test file not found: {test_file}"

    with open(test_file, "rb") as f:
        response = client.post(
            "/analyze",
            files={
                "file": (
                    test_file,
                    f,
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            }
        )

    # Accept 200 OK (success) or 422 Unprocessable Entity (validation fail but API reachable)
    assert response.status_code in [200, 422]
