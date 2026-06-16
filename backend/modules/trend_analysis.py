from modules.sql_analytics import (
    get_most_common_level,
    get_most_active_event,
    count_logs,
    count_errors
)


def generate_trend_analysis():

    print("\n===== TREND ANALYSIS =====")

    level = get_most_common_level()

    if level:
        print("\nMost Frequent Log Level:")
        print(level[0])

    event = get_most_active_event()

    if event:
        print("\nMost Active Event:")
        print(event[0])

    total_logs = count_logs()
    total_errors = count_errors()

    error_rate = (total_errors / total_logs) * 100

    print(f"\nError Rate: {error_rate:.2f}%")

    if error_rate > 30:
        print("Trend: HIGH ERROR ACTIVITY")
        print("System Status: NEEDS ATTENTION")

    elif error_rate > 10:
        print("Trend: MODERATE ERROR ACTIVITY")
        print("System Status: MONITOR")

    else:
        print("Trend: LOW ERROR ACTIVITY")
        print("System Status: HEALTHY")