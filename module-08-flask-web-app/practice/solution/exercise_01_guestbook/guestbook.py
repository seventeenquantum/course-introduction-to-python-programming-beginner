import sqlite3
from datetime import datetime

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
DB = "guestbook.db"


def get_conn():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    conn.execute(
        """CREATE TABLE IF NOT EXISTS entries (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               message TEXT NOT NULL,
               created TEXT NOT NULL
           )"""
    )
    return conn


@app.route("/", methods=["GET", "POST"])
def guestbook():
    errors = []
    name = ""
    message = ""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        message = request.form.get("message", "").strip()
        if not 1 <= len(name) <= 30:
            errors.append("Name must be 1 to 30 characters.")
        if not 1 <= len(message) <= 200:
            errors.append("Message must be 1 to 200 characters.")
        if not errors:
            conn = get_conn()
            conn.execute(
                "INSERT INTO entries (name, message, created) VALUES (?, ?, ?)",
                (name, message, datetime.now().strftime("%Y-%m-%d %H:%M")),
            )
            conn.commit()
            conn.close()
            return redirect(url_for("guestbook"))
    conn = get_conn()
    entries = conn.execute(
        "SELECT name, message, created FROM entries ORDER BY id DESC"
    ).fetchall()
    conn.close()
    return render_template(
        "guestbook.html", entries=entries, errors=errors, name=name, message=message
    )


if __name__ == "__main__":
    app.run(debug=True)
