"""Budget tracker (starter).

Menu: 1 Add transaction, 2 Monthly summary, 3 Quit.
Keep the maths in summarise() and do NO printing there, so it is easy to test.
"""

from datetime import datetime

from storage import load_transactions, save_transaction

FILE = "budget.csv"


def ask_date():
    """Keep asking until the user types a valid YYYY-MM-DD date.

    Hint: datetime.strptime(text, "%Y-%m-%d") raises ValueError for bad dates.
    """
    # TODO
    pass


def ask_amount():
    """Keep asking until the user types a number greater than zero."""
    # TODO
    pass


def ask_type():
    """Keep asking until the user types 'income' or 'expense'."""
    # TODO
    pass


def add_transaction():
    """Ask for a date, type, category and amount, then save the transaction."""
    # TODO
    pass


def summarise(transactions, month):
    """Return a dict with income, expenses, net and by_category for a month like '2026-09'.

    by_category only counts expenses, e.g. {"food": 200.0, "transport": 45.0}.
    """
    # TODO
    pass


def show_summary():
    """Ask for a month and print the summary using summarise()."""
    # TODO
    pass


def main():
    # TODO: the menu loop
    pass


if __name__ == "__main__":
    main()
