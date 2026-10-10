"""Create a throwaway folder of sample files to test the organiser on.

Run once:  python make_test_folder.py
NEVER test the organiser on your real Downloads folder first.
"""

from pathlib import Path

test = Path("test_downloads")
test.mkdir(exist_ok=True)
for name in [
    "report.pdf",
    "photo1.jpg",
    "photo2.PNG",
    "song.mp3",
    "notes.txt",
    "archive.zip",
    "script.py",
    "mystery",
]:
    (test / name).write_text("sample")
print(f"Created {test}/ with 8 sample files.")
