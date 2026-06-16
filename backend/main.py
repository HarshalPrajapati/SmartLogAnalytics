from modules.database_report import generate_report
from modules.csv_export import export_daily_report # type: ignore
from modules.insights import generate_insights # type: ignore
def main():

    print("\nStarting SmartLogAnalytics...\n")

    generate_report()

    generate_insights()

    print("\nGenerating CSV Report...\n")

    export_daily_report()

    print("\nSmartLogAnalytics Completed Successfully!")


if __name__ == "__main__":
    main()