from modules.sql_analytics import (
    count_logs,
    count_errors,
    get_most_common_level,
    get_most_active_event
)


def generate_executive_summary():

    print("\n===== EXECUTIVE SUMMARY =====")

    print(f"Total Logs Processed: {count_logs()}")
    print(f"Total Errors: {count_errors()}")

    level = get_most_common_level()
    event = get_most_active_event()

    if level:
        print(f"Dominant Log Level: {level[0]}")

    if event:
        print(f"Most Active Event: {event[0]}")