"""Exercise 1: Move the budget tracker to SQLite.

Copy this file over storage.py in your Week 4 budget tracker and change
FILE = "budget.csv" to FILE = "budget.db" in budget.py. Nothing else changes.
Then re-enter the Week 4 test data; the summaries must match.

Keep the function names load_transactions(path) and save_transaction(path, transaction).
Hint: conn.row_factory = sqlite3.Row makes rows act like dictionaries; dict(row) converts one.
"""

import sqlite3


def _connect(path):
    """Open the database and create the transactions table if needed.

    Columns: id, date, type (income or expense), category, amount (> 0).
    """
    # TODO
    pass


def load_transactions(path):
    # TODO
    pass


def save_transaction(path, transaction):
    # TODO
    pass
