import sys
from pathlib import Path

folder = Path(sys.argv[1])
prefix = sys.argv[2]
apply = "--apply" in sys.argv

files = sorted(folder.glob("*.jpg"))
for number, old in enumerate(files, start=1):
    new = old.with_name(f"{prefix}_{number:03d}{old.suffix.lower()}")
    if new.exists():
        print(f"Skipping {old.name}: {new.name} already exists")
        continue
    print(f"{old.name} -> {new.name}")
    if apply:
        old.rename(new)
