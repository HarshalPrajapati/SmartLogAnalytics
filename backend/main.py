from modules.parser import load_logs
from modules.analytics_engine import (
    count_log_levels,
    keyword_statistics,
    show_error_messages
)

logs = load_logs()

print("Total Logs:", len(logs))

print("\nLog Statistics:")
print(count_log_levels(logs))

print("\nKeyword Statistics:")
print(keyword_statistics(logs))

show_error_messages(logs)
