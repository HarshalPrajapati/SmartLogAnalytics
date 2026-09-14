import json
import os
import tempfile
from datetime import datetime

from dotenv import load_dotenv
from minio import Minio


load_dotenv()


def get_minio_client():
    endpoint = os.getenv("MINIO_ENDPOINT")
    access_key = os.getenv("MINIO_ACCESS_KEY")
    secret_key = os.getenv("MINIO_SECRET_KEY")

    return Minio(
        endpoint,
        access_key=access_key,
        secret_key=secret_key,
        secure=False
    )


def get_bucket_name():
    return os.getenv("MINIO_BUCKET")


def upload_file(file_path, object_name):
    client = get_minio_client()
    bucket_name = get_bucket_name()

    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)

    result = client.fput_object(
        bucket_name,
        object_name,
        file_path
    )

    return result


def upload_json(data, object_name):
    client = get_minio_client()
    bucket_name = get_bucket_name()

    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".json",
        delete=False
    ) as temp_file:

        if isinstance(data, list):
            for record in data:
                temp_file.write(
                    json.dumps(record) + "\n"
                )
        else:
            temp_file.write(
                json.dumps(data) + "\n"
            )

        temp_file_path = temp_file.name

    try:
        result = client.fput_object(
            bucket_name,
            object_name,
            temp_file_path,
            content_type="application/json"
        )

    finally:
        os.remove(temp_file_path)

    return result


def get_date_partition(timestamp=None):
    if timestamp:
        dt = datetime.strptime(
            timestamp,
            "%Y-%m-%d %H:%M:%S"
        )
    else:
        dt = datetime.now()

    return (
        f"year={dt.year}/"
        f"month={dt.month:02d}/"
        f"day={dt.day:02d}"
    )