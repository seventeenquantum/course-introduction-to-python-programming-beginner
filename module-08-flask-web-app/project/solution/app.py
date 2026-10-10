from datetime import date

from flask import Flask, abort, flash, redirect, render_template, request, url_for

from db import add_habit, check_in, connect, get_days, list_habits
from streaks import current_streak

app = Flask(__name__)
app.secret_key = "change-this-before-sharing"  # needed for flash messages


@app.route("/")
def index():
    conn = connect()
    today = date.today().isoformat()
    habits = []
    for habit_id, name in list_habits(conn):
        days = get_days(conn, habit_id)
        habits.append(
            {
                "id": habit_id,
                "name": name,
                "streak": current_streak(days),
                "done_today": today in days,
            }
        )
    conn.close()
    return render_template("index.html", habits=habits)


@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name", "").strip().lower()
    conn = connect()
    if not name:
        flash("Please type a habit name.")
    elif add_habit(conn, name):
        flash(f"Added {name}.")
    else:
        flash(f"{name} already exists.")
    conn.close()
    return redirect(url_for("index"))


@app.route("/checkin/<int:habit_id>", methods=["POST"])
def checkin(habit_id):
    conn = connect()
    if habit_id not in [h[0] for h in list_habits(conn)]:
        conn.close()
        abort(404)
    if check_in(conn, habit_id, date.today().isoformat()):
        flash("Checked in. Nice work!")
    else:
        flash("You already checked in today.")
    conn.close()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
