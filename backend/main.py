from modules.database_report import generate_report
from modules.csv_export import export_daily_report # type: ignore
from modules.insights import generate_insights # type: ignore
from modules.trend_analysis import generate_trend_analysis 
from modules.executive_summary import generate_executive_summary  # type: ignore
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

    print("\nGenerating CSV Report...\n")

    export_daily_report()

    print("\nSmartLogAnalytics Completed Successfully!")


if __name__ == "__main__":
    main()