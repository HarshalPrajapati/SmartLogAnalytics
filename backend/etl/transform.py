from modules.parser import parse_log_line


def transform_logs(raw_logs):

    transformed_logs = []

    for line in raw_logs:

        parsed_log = parse_log_line(line)

        if parsed_log is not None:
            transformed_logs.append(parsed_log)

    return transformed_logs
