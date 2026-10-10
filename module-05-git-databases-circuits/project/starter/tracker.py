"""Habit tracker menu (starter).

Menu: 1 Add habit, 2 Check in today, 3 Show streaks, 4 Quit.
Git reminder: commit after each module works, with a clear message.
"""

from datetime import date

from db import add_habit, check_in, connect, get_days, list_habits
from streaks import current_streak


def choose_habit(conn):
    """Print a numbered list of habits and return the chosen habit's id (or None)."""
    # TODO
    pass


def main():
    # TODO: connect, then loop over the menu
    pass


if __name__ == "__main__":
    main()
