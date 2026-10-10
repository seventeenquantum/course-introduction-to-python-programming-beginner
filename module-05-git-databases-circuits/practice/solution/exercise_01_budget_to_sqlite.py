"""Drop-in replacement for the Week 4 storage.py, using SQLite."""

import sqlite3


def _connect(path):
    conn = sqlite3.connect(path)
    conn.execute(
        """CREATE TABLE IF NOT EXISTS transactions (
               id INTEGER PRIMARY KEY,
               date TEXT NOT NULL,
               type TEXT NOT NULL CHECK (type IN ('income', 'expense')),
               category TEXT NOT NULL,
               amount REAL NOT NULL CHECK (amount > 0)
           )"""
    )
    return conn


def load_transactions(path):
    conn = _connect(path)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT date, type, category, amount FROM transactions ORDER BY date"
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]


def save_transaction(path, transaction):
    conn = _connect(path)
    conn.execute(
        "INSERT INTO transactions (date, type, category, amount) VALUES (?, ?, ?, ?)",
        (
            transaction["date"],
            transaction["type"],
            transaction["category"],
            transaction["amount"],
        ),
    )
    conn.commit()
    conn.close()


# Bonus: let the database do the maths. September spending by category, largest first:
#
#   SELECT category, SUM(amount) FROM transactions
#   WHERE type = 'expense' AND date LIKE '2026-09%'
#   GROUP BY category ORDER BY SUM(amount) DESC
