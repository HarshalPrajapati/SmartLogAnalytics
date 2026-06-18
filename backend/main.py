from modules.database_report import generate_report
from modules.csv_export import export_daily_report 
from modules.insights import generate_insights 
from modules.trend_analysis import generate_trend_analysis 
from modules.json_export import export_json_report  # type: ignore
from modules.dashboard_summary import show_dashboard_summary  # type: ignore
from modules.executive_summary import generate_executive_summary 
from modules.prioritization import ( # type: ignore
    generate_priority_report,
    generate_recommendations,
    generate_top_events_report
)

def main():

    print("\nStarting SmartLogAnalytics...\n")

    generate_report()

    generate_insights()

    generate_trend_analysis()

    generate_priority_report()

    generate_recommendations()

    generate_top_events_report()

    generate_executive_summary()

    show_dashboard_summary()

    print("\nGenerating CSV Report...\n")

    export_daily_report()

    print("\nGenerating JSON Report...\n")

    export_json_report("../reports/report.json")

    print("\nSmartLogAnalytics Completed Successfully!")


if __name__ == "__main__":
    main()