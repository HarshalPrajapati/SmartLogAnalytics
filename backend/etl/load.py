from modules.database import get_connection


def load_logs(logs):

    if not logs:
        return 0

    conn = get_connection()
    cur = conn.cursor()

    inserted_count = 0

    try:

        for log in logs:

            cur.execute(
                """
                INSERT INTO logs(timestamp, level, message)
                VALUES (%s, %s, %s)
                ON CONFLICT (timestamp, level, message)
                DO NOTHING
                """,
                (
                    log["timestamp"],
                    log["level"],
                    log["message"]
                )
            )

            if cur.rowcount == 1:
                inserted_count += 1

        conn.commit()

    except Exception:

        conn.rollback()
        raise

    finally:

        cur.close()
        conn.close()

    return inserted_count