def parse_log_line(line):

    parts = line.split()

    if len(parts) < 3:
        return None

    return {
        "timestamp": parts[0] + " " + parts[1],
        "level": parts[2],
        "message": " ".join(parts[3:])
    }


logs = []

with open("../logs/server.log", "r") as file:

    for line in file:

        parsed_log = parse_log_line(line)

        if parsed_log is not None:
            logs.append(parsed_log)


print("\n===== LOG ANALYTICS SUMMARY =====")

print("Total Logs:", len(logs))

level_counts = {}

for log in logs:

    level = log["level"]

    if level not in level_counts:
        level_counts[level] = 0

    level_counts[level] += 1


print("\nLog Level Counts:")

for level, count in level_counts.items():
    print(f"{level}: {count}")


print("\nError Messages:")
print("----------------")

for log in logs:

    if log["level"] == "ERROR":
        print(log["message"])

payment_count = 0
login_count = 0
database_count = 0

for log in logs:

    message = log["message"]

    if "Payment" in message:
        payment_count += 1

    if "Login" in message:
        login_count += 1

    if "Database" in message:
        database_count += 1


print("\nKeyword Analytics:")
print("------------------")
print("Payment Logs:", payment_count)
print("Login Logs:", login_count)
print("Database Logs:", database_count)
