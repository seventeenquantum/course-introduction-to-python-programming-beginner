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
    """Return the category folder name for a file, based on its extension."""
    extension = path.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    return "Other"


def unique_destination(destination):
    """If the destination exists, return a free name like 'report (1).pdf'."""
    if not destination.exists():
        return destination
    number = 1
    while True:
        candidate = destination.with_name(
            f"{destination.stem} ({number}){destination.suffix}"
        )
        if not candidate.exists():
            return candidate
        number += 1


def plan_moves(folder):
    """Return a list of (source, destination) pairs. Moves nothing."""
    moves = []
    for item in sorted(folder.iterdir()):
        if not item.is_file() or item.name.startswith("."):
            continue
        destination = folder / category_for(item) / item.name
        moves.append((item, unique_destination(destination)))
    return moves


def log(message):
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{stamp} {message}\n")


def organise(folder, apply=False):
    moves = plan_moves(folder)
    if not moves:
        print("Nothing to move.")
        return
    for source, destination in moves:
        if apply:
            destination.parent.mkdir(exist_ok=True)
            shutil.move(str(source), str(destination))
            log(f"MOVED {source} -> {destination}")
            print(f"Moved {source.name} -> {destination.parent.name}/")
        else:
            print(f"[dry run] {source.name} -> {destination.parent.name}/")
    if not apply:
        print("\nNo files were moved. Add --apply to do it for real.")


def main():
    if len(sys.argv) < 2:
        print("Usage: python organiser.py FOLDER [--apply]")
        return
    folder = Path(sys.argv[1])
    if not folder.is_dir():
        print(f"{folder} is not a folder.")
        return
    organise(folder, apply="--apply" in sys.argv)


if __name__ == "__main__":
    main()
