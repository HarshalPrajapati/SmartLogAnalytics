import json
import os
from datetime import datetime

from modules.minio_storage import upload_json


def quarantine_logs(invalid_logs):
    if not invalid_logs:
        return None

    os.makedirs("quarantine", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"rejected_{timestamp}.json"
    filepath = os.path.join("quarantine", filename)

    with open(filepath, "w") as file:
        json.dump(invalid_logs, file, indent=4)

    # Upload rejected records to MinIO
    upload_json(
        invalid_logs,
        f"quarantine/{filename}"
    )

    return filepath