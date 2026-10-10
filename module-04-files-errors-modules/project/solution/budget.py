from datetime import datetime

from storage import load_transactions, save_transaction

FILE = "budget.csv"


def ask_date():
    while True:
        text = input("Date (YYYY-MM-DD): ")
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return text
        except ValueError:
            print("Please use the format YYYY-MM-DD, for example 2026-09-15.")


def ask_amount():
    while True:
        text = input("Amount: ")
        try:
            amount = float(text)
        except ValueError:
            print("Please enter a number.")
            continue
        if amount <= 0:
            print("Amount must be greater than zero.")
            continue
        return amount


def ask_type():
    while True:
        kind = input("Type (income/expense): ").strip().lower()
        if kind in ("income", "expense"):
            return kind
        print("Please type income or expense.")


def add_transaction():
    transaction = {
        "date": ask_date(),
        "type": ask_type(),
        "category": input("Category: ").strip().lower(),
        "amount": ask_amount(),
    }
    save_transaction(FILE, transaction)
    print("Saved.")


def summarise(transactions, month):
    """Return income, expenses, net and spending by category for a month like '2026-09'."""
    income = 0.0
    expenses = 0.0
    by_category = {}
    for t in transactions:
        if not t["date"].startswith(month):
            continue
        if t["type"] == "income":
            income += t["amount"]
        else:
            expenses += t["amount"]
            by_category[t["category"]] = by_category.get(t["category"], 0) + t["amount"]
    return {
        "income": income,
        "expenses": expenses,
        "net": income - expenses,
        "by_category": by_category,
    }


def show_summary():
    month = input("Month (YYYY-MM): ")
    result = summarise(load_transactions(FILE), month)
    print(f"\nSummary for {month}")
    print(f"Income:   {result['income']:>10.2f}")
    print(f"Expenses: {result['expenses']:>10.2f}")
    print(f"Net:      {result['net']:>10.2f}")
    print("Spending by category:")
    totals = result["by_category"]
    for category in sorted(totals, key=totals.get, reverse=True):
        print(f"  {category:<12}{totals[category]:>10.2f}")


def main():
    while True:
        print("\n1 Add transaction  2 Monthly summary  3 Quit")
        choice = input("Choose: ")
        if choice == "1":
            add_transaction()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            break
        else:
            print("Please choose 1, 2 or 3.")


if __name__ == "__main__":
    main()
