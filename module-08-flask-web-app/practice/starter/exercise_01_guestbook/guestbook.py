"""Exercise 1: Guestbook page (starter).

A single page that shows a form (name and message) above a list of entries,
newest first. Submitting adds an entry to a SQLite table, including the time.
Validate: name 1 to 30 characters, message 1 to 200. On failure show the errors
and keep what the visitor typed in the form.

Manual tests: empty name (error shown); valid entry (appears at the top);
<script>alert(1)</script> as a message (shown as text, does not run).

Hints: one route can accept both methods with methods=["GET", "POST"];
check request.method. Jinja's {% for %}...{% else %}...{% endfor %} shows the
else part when the list is empty. Write templates/guestbook.html yourself.
"""

import sqlite3
from datetime import datetime

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
DB = "guestbook.db"


def get_conn():
    """Open the database, create the entries table if needed, return the connection."""
    # TODO
    pass


@app.route("/", methods=["GET", "POST"])
def guestbook():
    # TODO
    return "Guestbook coming soon"


if __name__ == "__main__":
    app.run(debug=True)
