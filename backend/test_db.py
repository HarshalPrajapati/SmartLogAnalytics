from modules.database import insert_log, fetch_all_logs

insert_log(
    "2026-06-12 12:00:00",
    "INFO",
    "Database Integration Successful"
)

logs = fetch_all_logs()

for log in logs:
    print(log)