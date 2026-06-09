def get_logs_by_level(logs, level):

    filtered_logs = []

    for log in logs:

        if log["level"] == level:
            filtered_logs.append(log)

    return filtered_logs


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


def get_top_errors(logs):

    error_counts = {}

    for log in logs:

        if log["level"] == "ERROR":

            message = log["message"]

            if message not in error_counts:
                error_counts[message] = 0

            error_counts[message] += 1

    return error_counts


def get_latest_error(logs):

    for log in reversed(logs):

        if log["level"] == "ERROR":
            return log

    return None


def get_error_logs(logs):

    results = []

    for log in logs:

        if log["level"] == "ERROR":
            results.append(log)

    return results


def sort_logs(logs):

    return sorted(
        logs,
        key=lambda log: log["timestamp"]
    )


def generate_report(logs):

    stats = count_log_levels(logs)

    print("\n====================================")
    print(" SMART LOG ANALYTICS REPORT ")
    print("====================================")

    print("\nSummary")
    print("-------")

    print(f"Total Logs: {len(logs)}")

    for level, count in stats.items():
        print(f"{level}: {count}")

    errors = get_top_errors(logs)

    print("\nTop Errors")
    print("----------")

    if errors:
        for error, count in errors.items():
            print(f"{error}: {count}")
    else:
        print("No errors found")

    latest_error = get_latest_error(logs)

    print("\nLatest Error")
    print("------------")

    if latest_error:
        print(f"Timestamp: {latest_error['timestamp']}")
        print(f"Message: {latest_error['message']}")
    else:
        print("No errors found")

    keywords = keyword_statistics(logs)

    print("\nKeyword Analytics")
    print("-----------------")

    for keyword, count in keywords.items():
        print(f"{keyword}: {count}")