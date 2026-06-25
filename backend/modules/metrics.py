from modules.metrics import calculate_metrics

from modules.log_viewer import get_recent_errors

from modules.dashboard_widgets import (
    get_top_errors,
    get_recent_activity
)


def get_dashboard_data():

    data = calculate_metrics()

    data["recent_errors"] = get_recent_errors()

    data["top_errors"] = get_top_errors()

    data["recent_activity"] = get_recent_activity()

    return data