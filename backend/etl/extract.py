import os

from modules.minio_storage import (
    upload_file,
    get_date_partition
)


def extract_logs():

    log_file = "../logs/server.log"

    if not os.path.exists(log_file):
        raise FileNotFoundError(
            f"Log file not found: {log_file}"
        )

    with open(log_file, "r") as file:
        logs = file.readlines()

    if logs:

        first_line = logs[0].strip()

        parts = first_line.split()

        if len(parts) >= 2:

            timestamp = (
                parts[0]
                + " "
                + parts[1]
            )

            partition = get_date_partition(
                timestamp
            )

            object_name = (
                f"raw/{partition}/server.log"
            )

            upload_file(
                log_file,
                object_name
            )

    return logs