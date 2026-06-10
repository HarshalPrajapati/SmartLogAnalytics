import psycopg2

try:
    connection = psycopg2.connect(
        host="10.255.255.254",
        database="smartloganalytics",
        user="postgres",
        password="admin"
    )

    print("Database Connected Successfully!")

    connection.close()

except Exception as e:
    print("Connection Failed:")
    print(e)