"""Downloads folder organiser (starter).

Usage:
  python organiser.py FOLDER            dry run: only shows what would happen
  python organiser.py FOLDER --apply    really moves the files and logs each move

Three safety habits: dry run first, log everything, never overwrite.
Test on the folder made by make_test_folder.py, NOT on your real Downloads.
"""

import shutil
import sys
from datetime import datetime
from pathlib import Path

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".tar", ".gz"],
    "Code": [".py", ".js", ".html"],
}
LOG_FILE = "organiser.log"


def category_for(path):
    """Return the category folder name for a file, based on its extension.

    Use path.suffix.lower(). Return "Other" if no category matches.
    """
    # TODO
    pass


def unique_destination(destination):
    """If the destination exists, return a free name like 'report (1).pdf'.

    Hints: destination.exists(), destination.stem, destination.suffix,
    destination.with_name(...)
    """
    # TODO
    pass


def plan_moves(folder):
    """Return a list of (source, destination) pairs. Moves NOTHING.

    Skip sub-folders and hidden files (names starting with ".").
    destination = folder / category / filename, made unique.
    Hint: sorted(folder.iterdir())
    """
    # TODO
    pass


def log(message):
    """Append a timestamped line to LOG_FILE."""
    # TODO
    pass


def organise(folder, apply=False):
    """Dry run by default. With apply=True: create the folder, shutil.move, log, print."""
    # TODO
    pass


def main():
    """Read the folder from sys.argv[1] and --apply from sys.argv."""
    # TODO
    pass


if __name__ == "__main__":
    main()
