GitHub Copilot: # Number Guessing Game

This is a simple number guessing game where the computer tries to guess a secret number that the user has in mind. The game is implemented in Python.

## How to Play

1. Run the `numberGuess.py` file in a Python environment.
2. The computer will start guessing numbers with binary search
3. The game ends when the computer correctly guesses the secret number.

## Code Overview

The `numberGuess.py` file contains the main code for the game. The game logic is implemented in a `while` loop that runs until the computer correctly guesses the secret number. The computer's guesses are generated using a binary search algorithm.

The game also calculates the expected number of attempts required to guess the secret number using the formula `log2(n)`, where `n` is the number of possible values. The calculated value is printed at the end of the game.

## Requirements

The game requires Python 3 to be installed on the system.
