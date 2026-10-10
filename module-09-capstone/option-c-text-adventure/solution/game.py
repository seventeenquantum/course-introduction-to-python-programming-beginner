import copy
import json

ROOMS = {
    "hall": {
        "description": "A dusty hall with a door to the north.",
        "exits": {"north": "library"},
        "items": ["key"],
    },
    "library": {
        "description": "Shelves of old books. A heavy door leads east.",
        "exits": {"south": "hall", "east": "vault"},
        "items": [],
    },
    "vault": {
        "description": "The vault. Treasure glints in the corner.",
        "exits": {"west": "library"},
        "items": ["treasure"],
    },
}
LOCKED = {"vault": "key"}  # room name -> item needed to enter


def new_world():
    return copy.deepcopy(ROOMS)


def new_player():
    return {"room": "hall", "inventory": [], "moves": 0}


def parse_command(text):
    """Turn 'go north' into ('go', 'north'). Return ('', '') for empty input."""
    words = text.strip().lower().split()
    if not words:
        return "", ""
    return words[0], " ".join(words[1:])


def describe(world, player):
    room = world[player["room"]]
    text = room["description"]
    if room["items"]:
        text += " You see: " + ", ".join(room["items"]) + "."
    return f"{text} Exits: {', '.join(room['exits'])}."


def go(world, player, direction):
    room = world[player["room"]]
    if direction not in room["exits"]:
        return "You can't go that way."
    target = room["exits"][direction]
    needed = LOCKED.get(target)
    if needed and needed not in player["inventory"]:
        return f"The {target} is locked. You need the {needed}."
    player["room"] = target
    player["moves"] += 1
    return describe(world, player)


def take(world, player, item):
    room = world[player["room"]]
    if item not in room["items"]:
        return f"There is no {item} here."
    room["items"].remove(item)
    player["inventory"].append(item)
    if item == "treasure":
        return "You take the treasure. You win!"
    return f"You take the {item}."


def save_game(path, world, player):
    with open(path, "w") as f:
        json.dump({"world": world, "player": player}, f, indent=2)


def load_game(path):
    """Return (world, player), or None if the file is missing or damaged."""
    try:
        with open(path) as f:
            data = json.load(f)
        return data["world"], data["player"]
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return None


def main():
    world = new_world()
    player = new_player()
    print(describe(world, player))
    while "treasure" not in player["inventory"]:
        verb, argument = parse_command(input("\n> "))
        if verb == "go":
            print(go(world, player, argument))
        elif verb == "take":
            print(take(world, player, argument))
        elif verb == "look":
            print(describe(world, player))
        elif verb == "inventory":
            print("You carry: " + (", ".join(player["inventory"]) or "nothing"))
        elif verb == "save":
            save_game("savegame.json", world, player)
            print("Game saved.")
        elif verb == "load":
            loaded = load_game("savegame.json")
            if loaded is None:
                print("No saved game found.")
            else:
                world, player = loaded
                print(describe(world, player))
        elif verb == "quit":
            print("Goodbye!")
            return
        else:
            print("Commands: go, take, look, inventory, save, load, quit")
    print(f"You won in {player['moves']} moves!")


if __name__ == "__main__":
    main()
