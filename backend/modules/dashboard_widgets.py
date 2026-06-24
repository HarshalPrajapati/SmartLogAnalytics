from modules.database import get_connection


def get_top_errors(limit=5):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT message, COUNT(*)
        FROM logs
        WHERE level = 'ERROR'
        GROUP BY message
        ORDER BY COUNT(*) DESC
        LIMIT %s
        """,
        (limit,)
    )

    results = cur.fetchall()

    cur.close()
    conn.close()

    return results


def get_recent_activity(limit=10):

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

    results = cur.fetchall()

    cur.close()
    conn.close()

    return results
