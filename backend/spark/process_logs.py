import os
from datetime import datetime

from dotenv import load_dotenv

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, lit

from pyspark.sql.types import (
    IntegerType,
    StringType,
    StructField,
    StructType,
    TimestampType,
    DecimalType
)

load_dotenv()


# --------------------------------------------------
# Configuration
# --------------------------------------------------

MINIO_ENDPOINT = os.getenv(
    "MINIO_ENDPOINT"
)

ACCESS_KEY = os.getenv(
    "MINIO_ACCESS_KEY"
)

SECRET_KEY = os.getenv(
    "MINIO_SECRET_KEY"
)

BUCKET = os.getenv(
    "MINIO_BUCKET"
)


DB_HOST = os.getenv(
    "DB_HOST",
    "localhost"
)

DB_PORT = os.getenv(
    "DB_PORT",
    "5432"
)

DB_NAME = os.getenv(
    "DB_NAME"
)

DB_USER = os.getenv(
    "DB_USER"
)

DB_PASSWORD = os.getenv(
    "DB_PASSWORD"
)


# --------------------------------------------------
# Spark Session
# --------------------------------------------------

def create_spark_session():

    return (
        SparkSession.builder

        .appName(
            "SmartLogAnalytics"
        )

        .master("local[*]")

        .config(
            "spark.jars.packages",
            ",".join([
                "org.apache.hadoop:hadoop-aws:3.5.0",
                "org.postgresql:postgresql:42.7.7"
            ])
        )

        # MinIO / S3A
        .config(
            "spark.hadoop.fs.s3a.endpoint",
            f"http://{MINIO_ENDPOINT}"
        )

        .config(
            "spark.hadoop.fs.s3a.access.key",
            ACCESS_KEY
        )

        .config(
            "spark.hadoop.fs.s3a.secret.key",
            SECRET_KEY
        )

        .config(
            "spark.hadoop.fs.s3a.path.style.access",
            "true"
        )

        .config(
            "spark.hadoop.fs.s3a.connection.ssl.enabled",
            "false"
        )

        .config(
            "spark.hadoop.fs.s3a.impl",
            "org.apache.hadoop.fs.s3a.S3AFileSystem"
        )

        .getOrCreate()
    )


# --------------------------------------------------
# Dynamic MinIO processed path
# --------------------------------------------------

def get_processed_path():

    log_file = "../logs/server.log"

    with open(log_file, "r") as file:
        first_line = file.readline().strip()

    parts = first_line.split()

    if len(parts) < 2:

        raise ValueError(
            "Unable to determine event date "
            "from log file"
        )

    timestamp = (
        parts[0]
        + " "
        + parts[1]
    )

    event_date = datetime.strptime(
        timestamp,
        "%Y-%m-%d %H:%M:%S"
    )

    partition = (
        f"year={event_date.year}/"
        f"month={event_date.month:02d}/"
        f"day={event_date.day:02d}"
    )

    return (
        f"s3a://{BUCKET}/"
        f"processed/{partition}/logs.json"
    )


# --------------------------------------------------
# Analytics path
# --------------------------------------------------

def get_analytics_path():

    return (
        f"s3a://{BUCKET}/"
        "analytics/log_level_counts"
    )


# --------------------------------------------------
# PostgreSQL JDBC configuration
# --------------------------------------------------

def get_postgres_url():

    return (
        f"jdbc:postgresql://"
        f"{DB_HOST}:{DB_PORT}/"
        f"{DB_NAME}"
    )


# --------------------------------------------------
# Load log events into warehouse
# --------------------------------------------------

def load_log_events(spark,df):

    print(
        "\n[10] Loading log events into "
        "PostgreSQL warehouse..."
    )

    warehouse_df = (
        df
        .withColumn(
            "event_date",
            col("timestamp").cast("date")
        )
        .withColumn(
            "timestamp",
            col("timestamp").cast("timestamp")
        )
        .select(
            "timestamp",
            "level",
            "message",
            "event_date"
        )
        .dropDuplicates(
            ["timestamp", "level", "message"]
        )
    )

    print(
        f"Records prepared for warehouse: "
        f"{warehouse_df.count()}"
    )

    warehouse_df.show(
        truncate=False
    )

    jdbc_url = get_postgres_url()

    properties = {
        "user": DB_USER,
        "password": DB_PASSWORD,
        "driver": "org.postgresql.Driver"
    }

    # Read existing warehouse records
    existing_df = (
        spark.read
        .jdbc(
            jdbc_url,
            "warehouse.log_events",
            properties=properties
        )
        .select(
            "timestamp",
            "level",
            "message"
        )
    )

    # Keep only records that are not already
    # present in the warehouse
    new_records_df = (
        warehouse_df.alias("new")
        .join(
            existing_df.alias("existing"),
            (
                (col("new.timestamp") == col("existing.timestamp"))
                &
                (col("new.level") == col("existing.level"))
                &
                (col("new.message") == col("existing.message"))
            ),
            "left_anti"
        )
    )

    new_count = new_records_df.count()

    print(
        f"New records to load: {new_count}"
    )

    if new_count > 0:

        (
            new_records_df
            .write
            .mode("append")
            .jdbc(
                jdbc_url,
                "warehouse.log_events",
                properties=properties
            )
        )

        print(
            "\nNew log events successfully "
            "loaded into warehouse.log_events"
        )

    else:

        print(
            "\nNo new log events to load."
        )


# --------------------------------------------------
# Load log level summary into warehouse
# --------------------------------------------------

def load_log_level_summary(
    analytics_df
):

    print(
        "\n[11] Loading log-level summary "
        "into PostgreSQL warehouse..."
    )

    summary_df = (
        analytics_df
        .select(
            col("level"),
            col("log_count"),
            col("percentage")
        )
    )

    summary_df.show()

    jdbc_url = get_postgres_url()

    properties = {
        "user": DB_USER,
        "password": DB_PASSWORD,
        "driver": "org.postgresql.Driver"
    }

    (
        summary_df
        .write
        .mode("overwrite")
        .jdbc(
            jdbc_url,
            "warehouse.log_level_summary",
            properties=properties
        )
    )

    print(
        "\nLog-level summary successfully "
        "loaded into warehouse.log_level_summary"
    )


# --------------------------------------------------
# Main
# --------------------------------------------------

def main():

    spark = create_spark_session()

    print(
        "\n===== SMARTLOGANALYTICS PYSPARK ====="
    )

    # --------------------------------------------------
    # 1. Read processed logs from MinIO
    # --------------------------------------------------

    print(
        "\n[1] Reading processed logs from MinIO..."
    )

    path = get_processed_path()

    print(
        f"Reading from: {path}"
    )

    df = spark.read.json(path)

    total_logs = df.count()

    print(
        f"Records loaded: {total_logs}"
    )

    # --------------------------------------------------
    # 2. Schema
    # --------------------------------------------------

    print("\n[2] Schema:")

    df.printSchema()

    # --------------------------------------------------
    # 3. Logs by level
    # --------------------------------------------------

    print("\n[3] Logs by Level:")

    level_counts = (
        df.groupBy("level")
        .agg(
            count("*").alias("count")
        )
        .orderBy(
            col("count").desc()
        )
    )

    level_counts.show()

    # --------------------------------------------------
    # 4. Error logs
    # --------------------------------------------------

    print("\n[4] Error Logs:")

    error_logs = df.filter(
        col("level") == "ERROR"
    )

    error_logs.show(
        truncate=False
    )

    # --------------------------------------------------
    # 5. Error rate
    # --------------------------------------------------

    print("\n[5] Error Rate:")

    total_errors = error_logs.count()

    if total_logs > 0:

        error_rate = (
            total_errors
            / total_logs
        ) * 100

        error_rate = round(
            error_rate,
            2
        )

    else:

        error_rate = 0

    print(
        f"Total Logs: {total_logs}"
    )

    print(
        f"Total Errors: {total_errors}"
    )

    print(
        f"Error Rate: {error_rate}%"
    )

    # --------------------------------------------------
    # 6. Analytics dataset
    # --------------------------------------------------

    print(
        "\n[6] Creating analytics dataset..."
    )

    analytics_df = (
        df.groupBy("level")
        .agg(
            count("*").alias(
                "log_count"
            )
        )
    )

    analytics_df.show()

    # --------------------------------------------------
    # 7. Log percentages
    # --------------------------------------------------

    print(
        "\n[7] Calculating log percentages..."
    )

    if total_logs > 0:

        percentage_df = (
            analytics_df
            .withColumn(
                "percentage",
                (
                    col("log_count")
                    / lit(total_logs)
                    * 100
                )
            )
        )

    else:

        percentage_df = (
            analytics_df
            .withColumn(
                "percentage",
                lit(0)
            )
        )

    percentage_df = (
        percentage_df
        .orderBy(
            col("log_count").desc()
        )
    )

    percentage_df.show()

    # --------------------------------------------------
    # 8. Processing timestamp
    # --------------------------------------------------

    print(
        "\n[8] Adding processing timestamp..."
    )

    analytics_df = (
        percentage_df
        .withColumn(
            "processed_at",
            lit(
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            )
        )
    )

    analytics_df.show()

    # --------------------------------------------------
    # 9. Write analytics to MinIO
    # --------------------------------------------------

    print(
        "\n[9] Writing analytics data "
        "to MinIO..."
    )

    analytics_path = (
        get_analytics_path()
    )

    (
        analytics_df
        .coalesce(1)
        .write
        .mode("overwrite")
        .json(analytics_path)
    )

    print(
        f"Analytics data written to: "
        f"{analytics_path}"
    )

    # --------------------------------------------------
    # 10. Load events into PostgreSQL
    # --------------------------------------------------

    load_log_events(spark, df)

    # --------------------------------------------------
    # 11. Load summary into PostgreSQL
    # --------------------------------------------------

    load_log_level_summary(
        analytics_df
    )

    # --------------------------------------------------
    # 12. Stop Spark
    # --------------------------------------------------

    print(
        "\n[12] Stopping Spark..."
    )

    spark.stop()

    print(
        "\n===== PYSPARK JOB COMPLETE ====="
    )


if __name__ == "__main__":
    main()