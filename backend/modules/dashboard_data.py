from modules.sql_analytics import (
    count_logs,
    count_errors,
    count_warnings,
    count_info,
    get_most_common_level,
    get_most_active_event
)
from modules.log_viewer import get_recent_errors

def get_dashboard_data():

    most_common_level = get_most_common_level()
    most_active_event = get_most_active_event()
    error_rate = 0

    if count_logs() > 0:
        error_rate = (count_errors() / count_logs()) * 100

    data = {
        "total_logs": count_logs(),
        "error_logs": count_errors(),
        "warning_logs": count_warnings(),
        "info_logs": count_info(),
        "error_rate": round(error_rate, 2),
        "most_common_level": (
            most_common_level[0]
            if most_common_level else None
        ),
        "most_active_event": (
            most_active_event[0]
            if most_active_event else None
        ),
        "system_health": (
            "CRITICAL"
            if error_rate > 30
            else "WARNING"
            if error_rate > 10
            else "HEALTHY"
        ),
        "recent_errors": get_recent_errors()
    }

    return data