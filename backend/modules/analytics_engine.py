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
