import csv
import os

FIELDS = ["date", "type", "category", "amount"]


def load_transactions(path):
    """Return a list of transaction dictionaries, or [] if there is no file yet."""
    if not os.path.exists(path):
        return []
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        row["amount"] = float(row["amount"])
    return rows


def save_transaction(path, transaction):
    """Append one transaction, writing the header first if the file is new."""
    is_new = not os.path.exists(path)
    with open(path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if is_new:
            writer.writeheader()
        writer.writerow(transaction)
