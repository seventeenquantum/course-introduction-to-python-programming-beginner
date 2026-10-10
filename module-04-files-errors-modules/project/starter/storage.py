"""Storage module for the budget tracker (starter).

Each transaction is a dictionary with the keys date, type, category, amount.
"""

import csv
import os

FIELDS = ["date", "type", "category", "amount"]


def load_transactions(path):
    """Return a list of transaction dictionaries, or [] if there is no file yet.

    Hints:
      - os.path.exists(path) tells you whether the file is there
      - open(path, newline="") and csv.DictReader(f)
      - the csv module reads everything as text: convert "amount" to float
    """
    # TODO
    pass


def save_transaction(path, transaction):
    """Append one transaction, writing the header row first if the file is new.

    Hints:
      - open(path, "a", newline="")
      - csv.DictWriter(f, fieldnames=FIELDS), writer.writeheader(), writer.writerow(...)
    """
    # TODO
    pass
