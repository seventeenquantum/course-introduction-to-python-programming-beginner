from datetime import date

from db import add_habit, check_in, connect, get_days, list_habits
from streaks import current_streak


def choose_habit(conn):
    habits = list_habits(conn)
    if not habits:
        print("No habits yet. Add one first.")
        return None
    for number, (habit_id, name) in enumerate(habits, start=1):
        print(f"{number}. {name}")
    choice = input("Which habit? ")
    if choice.isdigit() and 1 <= int(choice) <= len(habits):
        return habits[int(choice) - 1][0]
    print("That is not a valid choice.")
    return None


def main():
    conn = connect()
    while True:
        print("\n1 Add habit  2 Check in today  3 Show streaks  4 Quit")
        choice = input("Choose: ")
        if choice == "1":
            name = input("Habit name: ").strip().lower()
            if name and add_habit(conn, name):
                print("Added.")
            else:
                print("That habit already exists, or the name was empty.")
        elif choice == "2":
            habit_id = choose_habit(conn)
            if habit_id is not None:
                if check_in(conn, habit_id, date.today().isoformat()):
                    print("Checked in. Nice work!")
                else:
                    print("You already checked in today.")
        elif choice == "3":
            for habit_id, name in list_habits(conn):
                streak = current_streak(get_days(conn, habit_id))
                print(f"{name:<15}{streak} day streak")
        elif choice == "4":
            break
        else:
            print("Please choose 1, 2, 3 or 4.")
    conn.close()


if __name__ == "__main__":
    main()
