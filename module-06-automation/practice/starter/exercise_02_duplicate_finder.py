"""Exercise 2: Duplicate finder.

Usage:  python exercise_02_duplicate_finder.py FOLDER

Scan FOLDER and all its sub-folders and report groups of files with identical
contents, even if their names differ. NEVER delete anything.

Test setup: a.txt containing "hello", b.txt containing "hello", c.txt containing "world".
Expected: one group listing a.txt and b.txt. c.txt is not mentioned.

Hints: hashlib.sha256(path.read_bytes()).hexdigest() is a fingerprint of a file.
dict.setdefault(key, []) creates the list the first time you see a key.
Path.rglob("*") walks sub-folders.
"""

# TODO
