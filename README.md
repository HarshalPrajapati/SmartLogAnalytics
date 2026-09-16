# SmartLogAnalytics

A data engineering and log analytics platform that processes application logs through an ETL pipeline, stores data in MinIO and PostgreSQL, performs analytics using PySpark, orchestrates the workflow with Apache Airflow, and provides a Flask-based dashboard.

## Architecture

```text
Application Logs
       |
       v
 ETL Pipeline
       |
 +-----+------+
 |            |
 v            v
Validation  Data Quality
 |            |
 +-----+------+
       |
       v
     MinIO
       |
       v
    PySpark
       |
 +-----+------+
 |            |
 v            v
MinIO     PostgreSQL
Analytics  Warehouse
 |            |
 +-----+------+
       |
       v
 Flask Dashboard

Apache Airflow -> orchestrates ETL and PySpark
Docker Compose -> manages application and MinIO
```

## Features

- Application log ingestion
- Log parsing and transformation
- ETL pipeline
- Data validation
- Data quality reporting
- Invalid record quarantine
- Duplicate-safe database loading
- MinIO object storage
- Date-partitioned data
- PySpark batch analytics
- Log-level aggregation
- Error-rate calculation
- PostgreSQL analytical warehouse
- Flask dashboard
- CSV and JSON reporting
- Apache Airflow orchestration
- Docker containerization
- Docker Compose deployment
- Automated tests

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application and ETL |
| Flask | Web dashboard |
| PostgreSQL | Database and analytical warehouse |
| MinIO | Object storage / data lake |
| PySpark | Distributed log processing |
| Apache Airflow | Pipeline orchestration |
| Docker | Containerization |
| Docker Compose | Container management |
| Pandas | Data processing |
| Matplotlib | Visualization |
| SQL | Database analytics |
| Git/GitHub | Version control |

## Project Structure

```text
SmartLogAnalytics/
|
+-- backend/
|   +-- app.py
|   +-- main.py
|   +-- parse_logs.py
|   +-- run_pipeline.py
|   +-- etl/
|   +-- modules/
|   +-- spark/
|   |   +-- process_logs.py
|   +-- static/
|   +-- templates/
|   +-- test_charts.py
|   +-- test_dashboard.py
|   +-- test_json.py
|   +-- test_logs.py
|   +-- test_priority.py
|   +-- test_widgets.py
|   +-- requirements.txt
|
+-- airflow/
|   +-- dags/
|       +-- smartloganalytics_dag.py
|
+-- logs/
|   +-- server.log
|
+-- Dockerfile
+-- docker-compose.yml
+-- .dockerignore
+-- .gitignore
+-- README.md
```

## ETL Pipeline

The ETL pipeline is implemented in `backend/run_pipeline.py`.

### Extract
Reads application logs from `logs/server.log`.

### Transform
Parses log lines into structured records containing:

```text
timestamp
level
message
```

### Validate
Validates required fields, timestamp format, supported log levels, and non-empty messages.

Supported levels:

```text
INFO
WARNING
ERROR
```

### Data Quality
Generates reports containing total, valid, invalid records, success rate, failure rate, and validation errors.

### Quarantine
Separates invalid records for further investigation.

### Load
Loads valid records into PostgreSQL. Duplicate protection uses:

```text
timestamp + level + message
```

## MinIO Data Lake

MinIO provides the project's object-storage layer.

Example partitioning:

```text
raw/
  year=YYYY/
    month=MM/
      day=DD/
        server.log

processed/
  year=YYYY/
    month=MM/
      day=DD/
        logs.json

analytics/
  log_level_counts/
```

## PySpark Analytics

The PySpark job is:

```text
backend/spark/process_logs.py
```

It:

1. Reads processed logs from MinIO using S3A
2. Creates a Spark DataFrame
3. Aggregates logs by severity
4. Identifies ERROR logs
5. Calculates error rate
6. Calculates percentages by log level
7. Writes analytics to MinIO
8. Loads warehouse data into PostgreSQL

### Current Sample Results

```text
Total Logs: 12

INFO:     6  (50.00%)
ERROR:    4  (33.33%)
WARNING:  2  (16.67%)

Error Rate: 33.33%
```

## PostgreSQL Warehouse

The project uses a separate `warehouse` schema.

### warehouse.log_events

```text
id
log_id
timestamp
level
message
event_date
loaded_at
```

### warehouse.log_level_summary

```text
level
log_count
percentage
processed_at
```

This separates analytical data from the operational `logs` table.

## Apache Airflow

The DAG is located at:

```text
airflow/dags/smartloganalytics_dag.py
```

Workflow:

```text
run_etl_pipeline
       |
       v
run_pyspark
```

The ETL task runs first, followed by PySpark. Retry configuration is included.

## Docker

The Flask application is containerized using the project Dockerfile.

The image includes Python 3.12, the Java runtime required by PySpark, project dependencies, and the Flask application.

Application:

```text
http://localhost:5000
```

## Docker Compose

Docker Compose manages:

```text
smartloganalytics-app
smartloganalytics-minio
```

Start:

```bash
docker compose up -d --build
```

Check:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs
```

Stop:

```bash
docker compose down
```

## Configuration

Create locally:

```text
backend/.env
```

Example:

```env
DB_NAME=smartloganalytics
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=your_host
DB_PORT=5432

MINIO_ENDPOINT=minio:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin
MINIO_BUCKET=smartloganalytics
```

Never commit `.env` to GitHub.

## Running the ETL Pipeline

```bash
source .venv/bin/activate
cd backend
python run_pipeline.py
```

## Running PySpark

From the backend directory:

```bash
python spark/process_logs.py
```

## Running the Dashboard

```bash
docker compose up -d
```

Open:

```text
http://localhost:5000
```

## MinIO Console

Open:

```text
http://localhost:9001
```

## Testing

Tests currently cover charts, dashboard functionality, JSON handling, logs, prioritization, and widgets.

Run:

```bash
cd backend
python -m pytest
```

## End-to-End Workflow

```text
Application Log
       |
       v
     Extract
       |
       v
    Transform
       |
       v
    Validate
       |
       +------ Invalid ------> Quarantine
       |
       v
   Data Quality
       |
       v
      MinIO
       |
       v
     PySpark
       |
       +------> Analytics ------> MinIO
       |
       v
PostgreSQL Warehouse
       |
       v
Flask Dashboard
```

Airflow orchestrates the ETL and PySpark stages.

## Data Engineering Concepts Demonstrated

- ETL
- Data pipelines
- Data validation
- Data quality
- Data lake / object storage
- Data warehouse
- Batch processing
- Distributed processing
- PySpark
- SQL analytics
- Data partitioning
- Pipeline orchestration
- Database integration
- Containerization
- Docker Compose
- Analytics dashboards

## Future Improvements

- Kafka-based real-time log ingestion
- Spark Structured Streaming
- AWS S3 integration
- AWS Glue Data Catalog
- Amazon Redshift integration
- Advanced anomaly detection
- Automated error alerting
- CI/CD deployment
- Cloud deployment
- Monitoring and observability
- Authentication and role-based access

## Author

**Harshal Prajapati**

## License

This project is intended for educational and portfolio purposes.
