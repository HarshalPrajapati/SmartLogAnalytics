import psycopg2

def get_connection():
    return psycopg2.connect(
        database="smartloganalytics",
        user="harshal",
        password="harshal2912",
        host="localhost"
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