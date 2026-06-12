from modules.sql_analytics import (
    count_logs,
    count_errors,
    count_warnings,
    count_info,
    count_logins,
    count_payments,
    count_database_events,
    get_log_level_summary,
    get_error_messages
)


def generate_report():

    print("\n===== DATABASE ANALYTICS REPORT =====")

    print("\nTotal Logs:", count_logs())

    print("\nLog Levels")
    print("----------")

    for level, count in get_log_level_summary():
        print(f"{level}: {count}")

    print("\nKeyword Analytics")
    print("-----------------")
    print("Login Events:", count_logins())
    print("Payment Events:", count_payments())
    print("Database Events:", count_database_events())

    print("\nError Messages")
    print("--------------")

    errors = get_error_messages()

    if len(errors) == 0:
        print("No errors found.")

    else:
        for error in errors:
            print(error[0])