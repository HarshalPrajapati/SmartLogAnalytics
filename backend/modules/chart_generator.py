import matplotlib.pyplot as plt

from modules.sql_analytics import (
    count_errors,
    count_warnings,
    count_info
)


def generate_pie_chart():

    labels = ["INFO", "WARNING", "ERROR"]

    values = [
        count_info(),
        count_warnings(),
        count_errors()
    ]

    plt.figure(figsize=(6, 6))

    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%"
    )

    plt.title("Log Level Distribution")

    plt.savefig("static/images/log_level_pie.png")

    plt.close()


def generate_bar_chart():

    labels = ["INFO", "WARNING", "ERROR"]

    values = [
        count_info(),
        count_warnings(),
        count_errors()
    ]

    plt.figure(figsize=(6, 4))

    plt.bar(labels, values)

    plt.title("Log Level Counts")

    plt.xlabel("Log Level")

    plt.ylabel("Count")

    plt.savefig("static/images/log_level_bar.png")

    plt.close()
