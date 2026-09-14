import json
import os
from datetime import datetime


def generate_quality_report(
    logs,
    valid_logs,
    invalid_logs
):

    total_records = len(logs)
    valid_records = len(valid_logs)
    invalid_records = len(invalid_logs)

    success_rate = 0
    failure_rate = 0

    if total_records > 0:

        success_rate = round(
            (valid_records / total_records) * 100,
            2
        )

        failure_rate = round(
            (invalid_records / total_records) * 100,
            2
        )

    error_counts = {}

    for invalid in invalid_logs:

        for error in invalid["errors"]:

            if error not in error_counts:
                error_counts[error] = 0

            error_counts[error] += 1

    return {
        "total_records": total_records,
        "valid_records": valid_records,
        "invalid_records": invalid_records,
        "success_rate": success_rate,
        "failure_rate": failure_rate,
        "error_counts": error_counts
    }


def save_quality_report(report):

    os.makedirs(
        "quality_reports",
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = f"quality_{timestamp}.json"

    filepath = os.path.join(
        "quality_reports",
        filename
    )

    with open(filepath, "w") as file:

        json.dump(
            report,
            file,
            indent=4
        )

    return filepath


def print_quality_report(report):

    print("\n===== DATA QUALITY REPORT =====")

    print(
        f"\nTotal Records: {report['total_records']}"
    )

    print(
        f"Valid Records: {report['valid_records']}"
    )

    print(
        f"Invalid Records: {report['invalid_records']}"
    )

    print(
        f"\nSuccess Rate: {report['success_rate']}%"
    )

    print(
        f"Failure Rate: {report['failure_rate']}%"
    )

    print("\nValidation Errors:")

    if report["error_counts"]:

        for error, count in report["error_counts"].items():

            print(
                f"{error}: {count}"
            )

    else:

        print("No validation errors")