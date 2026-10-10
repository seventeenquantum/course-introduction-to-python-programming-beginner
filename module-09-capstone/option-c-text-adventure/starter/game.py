"""Text adventure (starter).

Model the world as a dictionary of rooms, keep the player's state in one
dictionary, and write one function per verb. Run `pytest` to check your work.

Commands to support: go <direction>, take <item>, look, inventory, save, load, quit.
You win by taking the treasure from the vault. The vault is locked until you
have the key.
"""

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
    """Return a fresh copy of ROOMS so one game never changes the original."""
    return copy.deepcopy(ROOMS)


def new_player():
    """Return {"room": "hall", "inventory": [], "moves": 0}."""
    # TODO
    pass


def parse_command(text):
    """Turn 'go north' into ('go', 'north'). Return ('', '') for empty input.

    Lower-case the text and strip extra spaces. Everything after the first
    word is the argument (so 'take old key' gives ('take', 'old key')).
    """
    # TODO
    pass


def describe(world, player):
    """Return the room description, plus 'You see: ...' if items are there, plus the exits."""
    # TODO
    pass


def go(world, player, direction):
    """Move through an exit. Refuse walls ("You can't go that way.")
    and locked rooms (message contains "locked"). Count moves. Return a message."""
    # TODO
    pass


def take(world, player, item):
    """Move an item from the room to the inventory. Return a message.
    Taking the treasure returns a message containing "win"."""
    # TODO
    pass


def save_game(path, world, player):
    """Write {"world": ..., "player": ...} to a JSON file."""
    # TODO
    pass


def load_game(path):
    """Return (world, player), or None if the file is missing or damaged."""
    # TODO
    pass


def main():
    """The game loop: read a command with input(), call the right function."""
    # TODO
    pass


if __name__ == "__main__":
    main()
