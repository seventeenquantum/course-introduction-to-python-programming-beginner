"""Number guessing game: worked solution."""

import random

secret = random.randint(1, 100)
max_attempts = 7
attempts = 0
won = False

print("I'm thinking of a number between 1 and 100.")

while attempts < max_attempts and not won:
    guess_text = input(f"Guess {attempts + 1} of {max_attempts}: ")
    if not guess_text.isdigit():
        print("Please enter a whole number.")
        continue
    guess = int(guess_text)
    attempts += 1
    if guess < secret:
        print("Too low.")
    elif guess > secret:
        print("Too high.")
    else:
        won = True

if won:
    print(f"You got it in {attempts} attempts!")
else:
    print(f"Out of attempts. The number was {secret}.")
