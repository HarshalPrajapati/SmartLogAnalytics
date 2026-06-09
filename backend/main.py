from modules.parser import load_logs

from modules.analytics_engine import (
    generate_report,
    sort_logs,
    get_logs_by_level,
    search_logs
)

# Load logs
logs = load_logs()

# Sort logs
logs = sort_logs(logs)

# Generate report
generate_report(logs)

# Example searches

print("\nERROR LOGS")
print("----------")

error_logs = get_logs_by_level(logs, "ERROR")

for log in error_logs:
    print(log)

print("\nPAYMENT LOGS")
print("------------")

payment_logs = search_logs(logs, "Payment")

for log in payment_logs:
    print(log)