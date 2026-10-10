def add_item(items, name):
    items.append(name)
    print(f"Added {name}.")


def remove_item(items, name):
    if name in items:
        items.remove(name)
        print(f"Removed {name}.")
    else:
        print(f"{name} is not on the list.")


def show_items(items):
    if not items:
        print("The list is empty.")
    for number, name in enumerate(items, start=1):
        print(f"{number}. {name}")


shopping = []
while True:
    print("\n1 Add  2 Remove  3 Show  4 Quit")
    choice = input("Choose: ")
    if choice == "1":
        add_item(shopping, input("Item: "))
    elif choice == "2":
        remove_item(shopping, input("Item: "))
    elif choice == "3":
        show_items(shopping)
    elif choice == "4":
        break
    else:
        print("Please choose 1, 2, 3 or 4.")
