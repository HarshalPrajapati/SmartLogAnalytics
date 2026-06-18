from modules.dashboard_data import get_dashboard_data


def show_dashboard_summary():

    data = get_dashboard_data()

    print("\n===== DASHBOARD SUMMARY =====")

    print("System Health:", data["system_health"])

    print("Error Rate:", data["error_rate"], "%")

    print("Most Common Level:",
          data["most_common_level"])

    print("Most Active Event:",
          data["most_active_event"])
