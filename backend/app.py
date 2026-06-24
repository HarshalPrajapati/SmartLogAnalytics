from flask import Flask, render_template
from modules.log_viewer import get_recent_logs
from modules.dashboard_data import get_dashboard_data
from modules.chart_generator import (generate_pie_chart,generate_bar_chart)
from modules.log_viewer import (get_recent_logs,get_logs_by_level)
from flask import (Flask,render_template,request)
from modules.log_viewer import (get_recent_logs,get_logs_by_level,search_logs)
from flask import (Flask,render_template,request,jsonify)

app = Flask(__name__)


@app.route("/")
def home():

    generate_pie_chart()
    generate_bar_chart()

    data = get_dashboard_data()

    return render_template(
        "dashboard.html",
        data=data
    )


@app.route("/dashboard")
def dashboard():

    return get_dashboard_data()

@app.route("/logs")
def logs():

    log_data = get_recent_logs()

    return render_template(
        "logs.html",
        logs=log_data
    )

@app.route("/logs/<level>")
def logs_by_level(level):

    log_data = get_logs_by_level(level.upper())

    return render_template(
        "logs.html",
        logs=log_data
    )

@app.route("/search")
def search():

    keyword = request.args.get(
        "q",
        ""
    )

    results = []

    if keyword:
        results = search_logs(keyword)

    return render_template(
        "search.html",
        logs=results,
        keyword=keyword
    )

@app.route("/api/stats")
def api_stats():

    data = get_dashboard_data()

    return jsonify({
        "total_logs": data["total_logs"],
        "error_logs": data["error_logs"],
        "warning_logs": data["warning_logs"],
        "info_logs": data["info_logs"],
        "error_rate": data["error_rate"],
        "system_health": data["system_health"]
    })

@app.route("/api/errors")
def api_errors():

    data = get_dashboard_data()

    return jsonify(data["top_errors"])

@app.route("/api/activity")
def api_activity():

    data = get_dashboard_data()

    return jsonify(data["recent_activity"])


if __name__ == "__main__":
    app.run(debug=True)
