from datetime import datetime, timedelta

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator


default_args = {
    "owner": "harshal",
    "retries": 2,
    "retry_delay": timedelta(minutes=1),
}


with DAG(
    dag_id="smartloganalytics_pipeline",
    start_date=datetime(2026, 9, 15),
    schedule=None,
    catchup=False,
    default_args=default_args,
    tags=["smartloganalytics", "data-engineering"],
) as dag:

    run_etl = BashOperator(
        task_id="run_etl_pipeline",
        bash_command=(
            "cd /home/harshal/SmartLogAnalytics/backend "
            "&& source /home/harshal/SmartLogAnalytics/.venv/bin/activate "
            "&& python run_pipeline.py"
        ),
    )

    run_pyspark = BashOperator(
        task_id="run_pyspark",
        bash_command=(
            "cd /home/harshal/SmartLogAnalytics/backend "
            "&& source /home/harshal/SmartLogAnalytics/.venv/bin/activate "
            "&& python spark/process_logs.py"
        ),
    )

    run_etl >> run_pyspark