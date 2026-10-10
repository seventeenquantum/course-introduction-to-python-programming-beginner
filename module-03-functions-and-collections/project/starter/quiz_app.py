"""Project: Command-line quiz app (starter).

Each question is a dictionary with three keys:
  question - the text
  options  - a list of 4 choices
  answer   - the text of the correct option

Fill in the three functions below, then call run_quiz(QUESTIONS) at the bottom.
"""

import random

QUESTIONS = [
    {
        "question": "Which keyword defines a function?",
        "options": ["func", "def", "define", "function"],
        "answer": "def",
    },
    {
        "question": "What does len([4, 5, 6]) return?",
        "options": ["2", "3", "4", "6"],
        "answer": "3",
    },
    {
        "question": "Which brackets create a dictionary?",
        "options": ["[ ]", "( )", "{ }", "< >"],
        "answer": "{ }",
    },
    {
        "question": "What does 'hello'.upper() return?",
        "options": ["hello", "Hello", "HELLO", "an error"],
        "answer": "HELLO",
    },
    {
        "question": "Which loop repeats a fixed number of times?",
        "options": ["for", "if", "def", "import"],
        "answer": "for",
    },
]


def ask_question(item, number):
    """Show one question, read the answer, return True if correct.

    Steps:
      1. Print "Question <number>: <question>".
      2. Print each option with a letter (a, b, c, d). Hint: enumerate().
      3. Keep asking until the player types a valid letter (a-d).
      4. Compare the chosen option's TEXT with item["answer"].
      5. Print "Correct!" or "Wrong. The answer was: ..." and return True/False.
    """
    # TODO
    pass


def show_result(score, total):
    """Print the final score, the percentage, and a short message."""
    # TODO
    pass


def run_quiz(questions):
    """Ask every question in random order and show the result.

    Hint: shuffle a COPY of the list (questions.copy()), not the original.
    """
    # TODO
    pass


# run_quiz(QUESTIONS)
