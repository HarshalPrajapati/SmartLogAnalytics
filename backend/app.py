from flask import Flask, render_template

from modules.dashboard_data import get_dashboard_data

app = Flask(__name__)


@app.route("/")
def home():

    data = get_dashboard_data()

    return render_template(
        "dashboard.html",
        data=data
    )


@app.route("/dashboard")
def dashboard():

    return get_dashboard_data()


if __name__ == "__main__":
    app.run(debug=True)