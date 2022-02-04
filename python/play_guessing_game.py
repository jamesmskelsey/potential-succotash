"""
Runs a guessing game.
"""

import random
from guessing_game import GuessingGame

game = GuessingGame(random.randint(1, 100))
last_guess = None
last_result = None

while not game.solved:
    if last_guess is not None:
        print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
        print("")

    last_guess = input("Enter your guess: ")
    last_result = game.guess(last_guess)


print(f"{last_guess} was correct!")
