import json

FILE = "contacts.json"


def load_contacts():
    try:
        with open(FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("The contact file is damaged. Starting with an empty book.")
        return {}


def save_contacts(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=2)


contacts = load_contacts()
while True:
    print("\n1 Add  2 Search  3 List  4 Quit")
    choice = input("Choose: ")
    if choice == "1":
        name = input("Name: ").strip()
        phone = input("Phone: ").strip()
        contacts[name.lower()] = {"name": name, "phone": phone}
        save_contacts(contacts)
        print("Saved.")
    elif choice == "2":
        term = input("Search for: ").strip().lower()
        found = [c for key, c in contacts.items() if term in key]
        if found:
            for c in found:
                print(f"{c['name']}: {c['phone']}")
        else:
            print("No matches.")
    elif choice == "3":
        for c in contacts.values():
            print(f"{c['name']}: {c['phone']}")
    elif choice == "4":
        break
    else:
        print("Please choose 1, 2, 3 or 4.")
