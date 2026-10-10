"""Exercise 1: Bulk file renamer.

Usage:  python exercise_01_renamer.py FOLDER PREFIX [--apply]

Rename every .jpg in FOLDER to PREFIX_001.jpg, PREFIX_002.jpg ... in
alphabetical order. Dry run by default; only rename with --apply.
Never overwrite an existing file.

Test setup: a folder "photos" containing b.jpg, a.jpg, c.jpg and notes.txt.
Expected: a.jpg -> holiday_001.jpg, b.jpg -> holiday_002.jpg, c.jpg -> holiday_003.jpg

Hints: sorted(folder.glob("*.jpg")), f"{number:03d}", old.with_name(...), old.rename(new)
"""

# TODO
