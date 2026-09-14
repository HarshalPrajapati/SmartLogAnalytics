import json
import os
from datetime import datetime


def quarantine_logs(invalid_logs):

    if not invalid_logs:
        return None

    os.makedirs("quarantine", exist_ok=True)

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = f"rejected_{timestamp}.json"

    filepath = os.path.join(
        "quarantine",
        filename
    )

    with open(filepath, "w") as file:

        json.dump(
            invalid_logs,
            file,
            indent=4
        )

    return filepath
