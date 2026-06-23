from modules.log_viewer import get_recent_logs

logs = get_recent_logs()

for log in logs:
    print(log)
