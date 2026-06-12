from modules.database import get_connection


def count_logs():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM logs")

    total = cur.fetchone()[0]

    cur.close()
    conn.close()

    return total


def count_errors():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT COUNT(*)
        FROM logs
        WHERE level = 'ERROR'
        """
    )

    total = cur.fetchone()[0]

    cur.close()
    conn.close()

    return total


def count_warnings():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT COUNT(*)
        FROM logs
        WHERE level = 'WARNING'
        """
    )

    total = cur.fetchone()[0]

    cur.close()
    conn.close()

    return total


def count_info():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT COUNT(*)
        FROM logs
        WHERE level = 'INFO'
        """
    )

    total = cur.fetchone()[0]

    cur.close()
    conn.close()

    return total

def count_logins():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT COUNT(*)
        FROM logs
        WHERE message LIKE '%Login%'
        """
    )

    total = cur.fetchone()[0]

    cur.close()
    conn.close()

    return total


def count_payments():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT COUNT(*)
        FROM logs
        WHERE message LIKE '%Payment%'
        """
    )

    total = cur.fetchone()[0]

    cur.close()
    conn.close()

    return total


def count_database_events():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT COUNT(*)
        FROM logs
        WHERE message LIKE '%Database%'
        """
    )

    total = cur.fetchone()[0]

    cur.close()
    conn.close()

    return total

def get_log_level_summary():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT level, COUNT(*)
        FROM logs
        GROUP BY level
        ORDER BY COUNT(*) DESC
        """
    )

    results = cur.fetchall()

    cur.close()
    conn.close()

    return results

def get_error_messages():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT message
        FROM logs
        WHERE level = 'ERROR'
        """
    )

    errors = cur.fetchall()

    cur.close()
    conn.close()

    return errors