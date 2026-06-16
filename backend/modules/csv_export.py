import csv
from datetime import datetime

from modules.sql_analytics import (
    count_logs,
    count_errors,
    count_warnings,
    count_info,
    count_logins,
    count_payments,
    count_database_events,
    get_top_errors,
    get_most_common_level,
    get_most_active_event
)


def export_report_csv(filename):

    data = [
        ["Metric", "Value"],
        ["Total Logs", count_logs()],
        ["ERROR Logs", count_errors()],
        ["WARNING Logs", count_warnings()],
        ["INFO Logs", count_info()],
        ["Login Events", count_logins()],
        ["Payment Events", count_payments()],
        ["Database Events", count_database_events()]
    ]

    top_errors = get_top_errors(1)

    if top_errors:
        data.append(["Top Error", top_errors[0][0]])
        data.append(["Top Error Count", top_errors[0][1]])

    most_common_level = get_most_common_level()
    most_active_event = get_most_active_event()

    if most_common_level:
        data.append(["Most Common Level", most_common_level[0]])

    if most_active_event:
        data.append(["Most Active Event", most_active_event[0]])

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerows(data)

    print(f"Report saved to {filename}")

def export_daily_report():

    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

    filename = f"../reports/report_{timestamp}.csv"

    export_report_csv(filename)

    