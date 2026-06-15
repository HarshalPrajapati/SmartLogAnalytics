import csv
from datetime import datetime

from modules.sql_analytics import (
    count_logs,
    count_errors,
    count_warnings,
    count_info,
    count_logins,
    count_payments,
    count_database_events
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

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerows(data)

    print(f"Report saved to {filename}")

def export_daily_report():

    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

    filename = f"../reports/report_{timestamp}.csv"

    export_report_csv(filename)