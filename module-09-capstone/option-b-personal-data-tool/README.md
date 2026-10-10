# Option B: Personal data tool

Build a tool that stores and queries data about something you care about, using
SQLite or a JSON file, with a command-line menu or a Flask page.

Idea starters: reading list with ratings, workout log with weekly totals, flashcards
with spaced review, expense splitter, recipe box with search by ingredient.

## Build order that works

1. Write down the one data record as a dictionary with 4 to 6 fields.
2. Write storage functions (`add`, `list`, `search`, `delete`) in their own module, with tests.
3. Write the interface (menu or Flask) as a thin layer that only calls those functions.
4. Add one "insight" feature: a weekly total, a streak, or the top five items.
5. Validate every input: empty file, duplicate, text where a number should be.

There is no solution folder because the project is yours. Reuse patterns from
Weeks 3 to 5 (storage module + tests) and Week 8 (Flask).
Copy `../templates/BRIEF.md` into your project folder before you write any code.
