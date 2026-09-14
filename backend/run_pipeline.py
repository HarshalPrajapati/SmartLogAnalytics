from etl.extract import extract_logs
from etl.transform import transform_logs
from etl.validate import validate_logs
from etl.data_quality import (
    generate_quality_report,
    print_quality_report,
    save_quality_report
)
from etl.quarantine import quarantine_logs
from etl.load import load_logs
from modules.minio_storage import (
    upload_json,
    get_date_partition
)


def run_pipeline():

    print("\n===== SMARTLOGANALYTICS ETL PIPELINE =====")

    # --------------------------------------------------
    # 1. EXTRACT
    # --------------------------------------------------

    print("\n[1] Extracting logs...")

    raw_logs = extract_logs()

    print(
        f"Extracted: {len(raw_logs)} records"
    )

    # --------------------------------------------------
    # 2. TRANSFORM
    # --------------------------------------------------

    print("\n[2] Transforming logs...")

    transformed_logs = transform_logs(
        raw_logs
    )

    print(
        f"Transformed: {len(transformed_logs)} records"
    )

    # --------------------------------------------------
    # 3. VALIDATE
    # --------------------------------------------------

    print("\n[3] Validating logs...")

    valid_logs, invalid_logs = validate_logs(
        transformed_logs
    )

    print(
        f"Valid: {len(valid_logs)} records"
    )

    print(
        f"Invalid: {len(invalid_logs)} records"
    )

    # --------------------------------------------------
    # 4. DATA QUALITY REPORT
    # --------------------------------------------------

    report = generate_quality_report(
        transformed_logs,
        valid_logs,
        invalid_logs
    )

    print_quality_report(report)

    quality_report_file = save_quality_report(
        report
    )

    print(
        f"\nQuality report saved: {quality_report_file}"
    )

    # --------------------------------------------------
    # 5. QUARANTINE INVALID RECORDS
    # --------------------------------------------------

    if invalid_logs:

        print(
            "\n[5] Quarantining invalid records..."
        )

        quarantine_file = quarantine_logs(
            invalid_logs
        )

        print(
            f"Quarantine file: {quarantine_file}"
        )

    else:

        print(
            "\n[5] No invalid records to quarantine"
        )

    # --------------------------------------------------
    # 6. LOAD VALID RECORDS
    # --------------------------------------------------

    print("\n[6] Uploading processed data to MinIO...")

    if valid_logs:

        partition = get_date_partition(
            valid_logs[0]["timestamp"]
        )

        upload_json(
            valid_logs,
            f"processed/{partition}/logs.json"
    )

    print("Processed data uploaded to MinIO")

    print(
        "\n[7] Loading valid records..."
    )

    inserted = load_logs(valid_logs)

    print(
        f"New records loaded: {inserted}"
    )

    print(
        "\n===== ETL PIPELINE COMPLETE ====="
    )


if __name__ == "__main__":

    run_pipeline()