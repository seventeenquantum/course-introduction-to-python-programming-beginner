"""Command-line quiz app: worked solution."""

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
    """Show one question, read the answer, return True if correct."""
    letters = "abcd"
    print(f"\nQuestion {number}: {item['question']}")
    for i, option in enumerate(item["options"]):
        print(f"  {letters[i]}) {option}")

    while True:
        choice = input("Your answer: ").strip().lower()
        if len(choice) == 1 and choice in letters:
            break
        print("Please type a, b, c or d.")

    chosen = item["options"][letters.index(choice)]
    if chosen == item["answer"]:
        print("Correct!")
        return True
    print(f"Wrong. The answer was: {item['answer']}")
    return False


def show_result(score, total):
    """Print the final score and a short message."""
    percent = score / total * 100
    print(f"\nYou scored {score} out of {total} ({percent:.0f}%).")
    if percent == 100:
        print("Perfect!")
    elif percent >= 60:
        print("Well done.")
    else:
        print("Keep practising.")


def run_quiz(questions):
    """Ask every question in random order and show the result."""
    shuffled = questions.copy()
    random.shuffle(shuffled)
    score = 0
    for number, item in enumerate(shuffled, start=1):
        if ask_question(item, number):
            score += 1
    show_result(score, len(shuffled))


if __name__ == "__main__":
    run_quiz(QUESTIONS)
