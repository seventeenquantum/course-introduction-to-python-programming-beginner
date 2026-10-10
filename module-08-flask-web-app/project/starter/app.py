"""Habit tracker web app (starter).

pip install flask pytest
Run:  python app.py   then open http://127.0.0.1:5000

db.py and streaks.py are the Week 5 modules, unchanged.

Step 1: get "Hello, habits!" on screen.
Step 2: fill in templates/base.html and templates/index.html.
Step 3: write the routes below. Remember post-redirect-get: after handling a
        form, redirect to a normal GET page so a refresh does not resubmit it.
Step 4: run `pytest` and the manual test table from the workbook.
"""

from datetime import date

from flask import Flask, abort, flash, redirect, render_template, request, url_for

from db import add_habit, check_in, connect, get_days, list_habits
from streaks import current_streak

app = Flask(__name__)
app.secret_key = "change-this-before-sharing"  # needed for flash messages


@app.route("/")
def index():
    """Show every habit with its streak and whether it is done today.

    Build a list of dicts with id, name, streak and done_today, then
    render_template("index.html", habits=habits). Open and close one
    database connection per request.
    """
    return "Hello, habits!"  # TODO: replace with the real page


@app.route("/add", methods=["POST"])
def add():
    """Read request.form["name"], add the habit, flash a message, redirect to index."""
    # TODO
    pass


@app.route("/checkin/<int:habit_id>", methods=["POST"])
def checkin(habit_id):
    """Check in for today. abort(404) if the habit does not exist. Flash, then redirect."""
    # TODO
    pass


if __name__ == "__main__":
    app.run(debug=True)
