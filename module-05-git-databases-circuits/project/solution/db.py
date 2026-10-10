import sqlite3


def connect(path="habits.db"):
    """Open the database and create the tables if they do not exist."""
    conn = sqlite3.connect(path)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute(
        """CREATE TABLE IF NOT EXISTS habits (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL UNIQUE
           )"""
    )
    conn.execute(
        """CREATE TABLE IF NOT EXISTS checkins (
               id INTEGER PRIMARY KEY,
               habit_id INTEGER NOT NULL REFERENCES habits(id),
               day TEXT NOT NULL,
               UNIQUE (habit_id, day)
           )"""
    )
    conn.commit()
    return conn


def add_habit(conn, name):
    """Return True if added, False if the habit already exists."""
    try:
        conn.execute("INSERT INTO habits (name) VALUES (?)", (name,))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False


def list_habits(conn):
    return conn.execute("SELECT id, name FROM habits ORDER BY name").fetchall()


def check_in(conn, habit_id, day):
    """Return True if recorded, False if already checked in that day."""
    try:
        conn.execute(
            "INSERT INTO checkins (habit_id, day) VALUES (?, ?)", (habit_id, day)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False


def get_days(conn, habit_id):
    rows = conn.execute(
        "SELECT day FROM checkins WHERE habit_id = ? ORDER BY day DESC", (habit_id,)
    ).fetchall()
    return [row[0] for row in rows]
