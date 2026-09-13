from datetime import datetime


VALID_LEVELS = {"INFO", "WARNING", "ERROR"}


def validate_log(log):

    errors = []

    # Check required fields
    required_fields = ["timestamp", "level", "message"]

    for field in required_fields:

        if field not in log:
            errors.append(f"Missing field: {field}")

    # Stop further validation if required fields are missing
    if errors:
        return False, errors

    # Validate timestamp
    try:

        datetime.strptime(
            log["timestamp"],
            "%Y-%m-%d %H:%M:%S"
        )

    except ValueError:

        errors.append("Invalid timestamp")

    # Validate log level
    if log["level"] not in VALID_LEVELS:

        errors.append(
            f"Invalid log level: {log['level']}"
        )

    # Validate message
    if not log["message"].strip():

        errors.append("Empty message")

    if errors:

        return False, errors

    return True, []

def validate_logs(logs):

    valid_logs = []
    invalid_logs = []

    for log in logs:

        is_valid, errors = validate_log(log)

        if is_valid:

            valid_logs.append(log)

        else:

            invalid_logs.append({
                "log": log,
                "errors": errors
            })

    return valid_logs, invalid_logs

