import os

import psycopg2
from dotenv import load_dotenv


load_dotenv()


def get_connection():

    return psycopg2.connect(
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST")
    )


def insert_log(timestamp, level, message):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO logs(timestamp, level, message)
        VALUES (%s, %s, %s)
        """,
        (timestamp, level, message)
    )

    conn.commit()

    cur.close()
    conn.close()


def fetch_all_logs():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM logs")

    logs = cur.fetchall()

    cur.close()
    conn.close()

    return logs