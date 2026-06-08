def parse_log_line(line):

    parts = line.split()

    if len(parts) < 3:
        return None

    return {
        "timestamp": parts[0] + " " + parts[1],
        "level": parts[2],
        "message": " ".join(parts[3:])
    }


def load_logs():

    logs = []

    with open("../logs/server.log", "r") as file:

        for line in file:

            parsed_log = parse_log_line(line)

            if parsed_log:
                logs.append(parsed_log)

    return logs
