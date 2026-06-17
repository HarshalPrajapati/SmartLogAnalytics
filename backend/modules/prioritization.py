from modules.sql_analytics import get_top_5_errors
from modules.sql_analytics import get_top_5_events

def classify_severity(count):

    if count >= 5:
        return "HIGH"

    elif count >= 3:
        return "MEDIUM"

    else:
        return "LOW"


def generate_priority_report():

    print("\n===== PRIORITY ISSUES =====")

    errors = get_top_5_errors()

    if not errors:
        print("No errors found.")
        return

    for index, (message, count) in enumerate(errors, start=1):

        severity = classify_severity(count)

        print(
            f"{index}. [{severity}] "
            f"{message} ({count} occurrences)"
        )

def generate_recommendations():

    print("\n===== RECOMMENDATIONS =====")

    errors = get_top_5_errors()

    if not errors:
        print("System operating normally.")
        return

    top_error = errors[0]

    message = top_error[0]
    count = top_error[1]

    print(
        f"Primary issue detected: "
        f"{message}"
    )

    if count >= 5:
        print(
            "Recommendation: Immediate investigation required."
        )

    elif count >= 3:
        print(
            "Recommendation: Monitor and investigate."
        )

    else:
        print(
            "Recommendation: Continue monitoring."
        )

def generate_top_events_report():

    print("\n===== TOP SYSTEM EVENTS =====")

    events = get_top_5_events()

    if not events:
        print("No events found.")
        return

    for index, (message, count) in enumerate(events, start=1):

        print(
            f"{index}. {message} "
            f"({count} occurrences)"
        )