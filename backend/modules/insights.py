from modules.sql_analytics import (
    get_top_messages,
    get_top_errors,
    count_errors,
    count_logs
)


def generate_insights():

    print("\n===== INSIGHTS =====")

    top_messages = get_top_messages()
    top_errors = get_top_errors()

    if top_messages:

        message, count = top_messages[0]

        print("\nMost Common Activity:")
        print(f"{message} ({count} occurrences)")

    if top_errors:

        error, count = top_errors[0]

        print("\nMost Common Error:")
        print(f"{error} ({count} occurrences)")

    total_logs = count_logs()
    total_errors = count_errors()

    print("\nSystem Health:")

    error_percentage = (total_errors / total_logs) * 100

    print(f"Error Rate: {error_percentage:.2f}%")

    if error_percentage > 30:
        print("Recommendation: High error rate detected. Investigate immediately.")

    elif error_percentage > 10:
        print("Recommendation: Monitor system for recurring issues.")

    else:
        print("Recommendation: System appears healthy.")