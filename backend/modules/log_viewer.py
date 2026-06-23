from modules.database import get_connection


def get_recent_logs(limit=20):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT timestamp, level, message
        FROM logs
        ORDER BY id DESC
        LIMIT %s
        """,
        (limit,)
    )

    logs = cur.fetchall()

    cur.close()
    conn.close()

    return logs


def get_logs_by_level(level):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT timestamp, level, message
        FROM logs
        WHERE level = %s
        ORDER BY id DESC
        """,
        (level,)
    )

    logs = cur.fetchall()

    cur.close()
    conn.close()

    return logs


def search_logs(keyword):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT timestamp, level, message
        FROM logs
        WHERE message ILIKE %s
        ORDER BY id DESC
        """,
        (f"%{keyword}%",)
    )

    logs = cur.fetchall()

    cur.close()
    conn.close()

    return logs


def get_recent_errors(limit=5):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT timestamp, message
        FROM logs
        WHERE level = 'ERROR'
        ORDER BY id DESC
        LIMIT %s
        """,
        (limit,)
    )

    errors = cur.fetchall()

    cur.close()
    conn.close()

    return errors