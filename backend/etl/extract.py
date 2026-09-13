import os


def extract_logs():

    log_file = "../logs/server.log"

    if not os.path.exists(log_file):
        raise FileNotFoundError(
            f"Log file not found: {log_file}"
        )

    with open(log_file, "r") as file:

        logs = file.readlines()

    return logs
