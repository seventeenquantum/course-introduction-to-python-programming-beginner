"""Database module for the habit tracker (starter).

Two tables:
  habits:    id (primary key), name (text, unique)
  checkins:  id (primary key), habit_id (refers to habits.id), day (YYYY-MM-DD)
             and the pair (habit_id, day) must be UNIQUE.

This module only talks to the database. It never prints or asks questions.
ALWAYS pass values with ? placeholders. Never build SQL with f-strings.
"""

import sqlite3


def connect(path="habits.db"):
    """Open the database, create both tables if they do not exist, return the connection."""
    # TODO
    pass


def add_habit(conn, name):
    """Return True if added, False if the habit already exists (IntegrityError)."""
    # TODO
    pass


def list_habits(conn):
    """Return a list of (id, name) tuples ordered by name."""
    # TODO
    pass


def check_in(conn, habit_id, day):
    """Return True if recorded, False if already checked in that day."""
    # TODO
    pass


def get_days(conn, habit_id):
    """Return the list of day strings for a habit, newest first."""
    # TODO
    pass
