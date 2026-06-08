def parse_log_line(line):

    parts = line.split()

    if len(parts) < 3:
        return None

    return {
        "timestamp": parts[0] + " " + parts[1],
        "level": parts[2],
        "message": " ".join(parts[3:])
    }

def get_logs_by_level(logs, level):

    filtered_logs = []

    for log in logs:

        if log["level"] == level:
            filtered_logs.append(log)

    return filtered_logs

def load_logs():

    logs = []

    with open("../logs/server.log", "r") as file:

        for line in file:

            parsed_log = parse_log_line(line)

            if parsed_log:
                logs.append(parsed_log)

    return logs

def search_logs(logs, keyword):

    results = []

    for log in logs:

        if keyword.lower() in log["message"].lower():
            results.append(log)

    return results

def count_log_levels(logs):

    level_counts = {}

    for log in logs:

        level = log["level"]

        if level not in level_counts:
            level_counts[level] = 0

        level_counts[level] += 1

    return level_counts

def generate_dashboard(logs):

    stats = count_log_levels(logs)

    print("\n==========================")
    print(" LOG ANALYTICS DASHBOARD ")
    print("==========================")

    print(f"\nTotal Logs: {len(logs)}")

    print("\nLog Levels:")

    for level, count in stats.items():
        print(f"{level}: {count}")

def show_error_messages(logs):

    print("\nERROR MESSAGES")
    print("----------------")

    for log in logs:

        if log["level"] == "ERROR":
            print(log["message"])

def keyword_statistics(logs):

    keywords = {
        "Payment": 0,
        "Login": 0,
        "Database": 0
    }

    for log in logs:

        message = log["message"]

        for keyword in keywords:

            if keyword.lower() in message.lower():
                keywords[keyword] += 1

    return keywords

logs = load_logs()

generate_dashboard(logs)

show_error_messages(logs)

keyword_stats = keyword_statistics(logs)

print("\nKEYWORD ANALYTICS")

for keyword, count in keyword_stats.items():
    print(f"{keyword}: {count}")
