# Python from Zero

Starter and worked-solution code for every project and practice exercise in the
9-Module course **Python from Zero: Build Real Things**.

## How the folders work

```text
module-NN-name/
  project/
    starter/    skeleton with TODOs and hints (and tests that fail until you finish)
    solution/   the worked version
  practice/
    starter/    one file per exercise, with the task in the docstring
    solution/   worked answers
```

Module 9 is different: it has three capstone options (A circuit simulator, B personal
data tool, C text adventure) plus a brief template, a rubric and a reflection template.

**Learners:** copy a `starter` folder, work in the copy, and only open `solution` after
you have tried.

## Setup

```text
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running things

Run a script from inside its own folder, because some projects read and write files
next to themselves:

```text
cd module-02-decisions-and-loops/project/solution
python guessing_game.py
```

Run tests from inside the folder too, not from the repository root. Several folders
contain files with the same name (`test_app.py`, for example), so pytest would get
confused if you ran them all at once.

```text
cd module-04-files-errors-modules/project/solution
pytest
```

To test every solution at once on Linux or Mac: `bash scripts/run_solution_tests.sh`.
The included GitHub Actions workflow (`.github/workflows/tests.yml`) does the same on
every push.
