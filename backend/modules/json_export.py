import json

from modules.dashboard_data import get_dashboard_data # type: ignore


def export_json_report(filename):

    data = get_dashboard_data()

    with open(filename, "w") as file:
        json.dump(
            data,
            file,
            indent=4
        )

    print(f"JSON report saved to {filename}")
