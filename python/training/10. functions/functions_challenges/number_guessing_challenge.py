# Number Guessing Game Challenge

# Your task is to complete a number guessing game.
# The game should be able to choose a random number between 1 and 100, and the user should be able to guess the number.
# Based on the user's guess, the game should provide feedback if the guess is too low, too high, or correct.
# Additionally, the game should have two difficulty levels, easy and hard. In the easy mode, the user gets 10 attempts, while in the hard mode, the user gets 5 attempts.

# Hints:
# 1. Start by setting up the game's main structure. Define the main game function and the loops required.
# 2. Implement the functionality to choose a random number.
# 3. Define functions to check the user's guess and to set the game's difficulty.
# 4. Keep track of the number of turns the user has and end the game if they run out of turns.

# Here are some lines from the solution to help you out:

from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    # Your code here


def set_difficulty():
    # Your code here


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    # Continue with the game logic...


# Start the game by calling the game function
game()
