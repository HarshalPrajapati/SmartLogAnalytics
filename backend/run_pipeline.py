from etl.extract import extract_logs
from etl.transform import transform_logs
from etl.validate import validate_logs
from etl.load import load_logs


def run_pipeline():

    print("\n===== SMARTLOGANALYTICS ETL PIPELINE =====")

    # EXTRACT
    print("\n[1] Extracting logs...")

    raw_logs = extract_logs()

    print(f"Extracted: {len(raw_logs)} records")

    # TRANSFORM
    print("\n[2] Transforming logs...")

    transformed_logs = transform_logs(raw_logs)

    print(f"Transformed: {len(transformed_logs)} records")

    # VALIDATE
    print("\n[3] Validating logs...")

    valid_logs, invalid_logs = validate_logs(
        transformed_logs
    )

    print(f"Valid: {len(valid_logs)} records")
    print(f"Invalid: {len(invalid_logs)} records")

    # LOAD
    print("\n[4] Loading valid logs...")

    inserted = load_logs(valid_logs)

    print(f"Loaded: {inserted} records")

    print("\n===== ETL PIPELINE COMPLETE =====")


if __name__ == "__main__":
    run_pipeline()
