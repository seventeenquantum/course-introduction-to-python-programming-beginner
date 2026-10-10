import hashlib
import sys
from pathlib import Path


def file_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


groups = {}
for path in Path(sys.argv[1]).rglob("*"):
    if path.is_file():
        groups.setdefault(file_hash(path), []).append(path)

found = False
for paths in groups.values():
    if len(paths) > 1:
        found = True
        print("Duplicates:")
        for p in sorted(paths):
            print(f"  {p}")
if not found:
    print("No duplicates found.")
