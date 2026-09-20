# Blackjack Game Challenge

"""
Your task is to create a simple version of the Blackjack game using Python.
Use the hints and structure below to guide you in building the game.

Objective:
You and the computer both draw cards from a deck. The goal is to have the highest hand without going over 21. 
Aces can be counted as 11 or 1, and face cards are all worth 10.
"""

############### Hints and Structure #####################

# Hint 1: Familiarize yourself with the game of Blackjack.
# Hint 2: Create functions for the different parts of the game logic.

import random

# TODO: Use the function below as a starting point to deal a card:


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# TODO: Build on the function below to calculate the score of a hand:


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Add conditions for handling the Ace card
    # ... your code here ...

# Hint 3: Consider how you will structure the game loop.
# Hint 4: Implement game rules, e.g., if the player's score goes over 21, they lose.

# TODO: Create a function to compare scores of the player and the computer:


def compare(user_score, computer_score):
    # Implement conditions to determine the winner
    # ... your code here ...

    # Hint 5: Consider adding features like clearing the console and displaying a game logo.

    # TODO: Build the main function that drives the game:


def play_game():
    # Implement the game logic here
    # ... your code here ...

    # TODO: Create a loop to restart the game if the player wishes:
    # ... your code here ...
    # Blackjack Game Challenge

"""
Your task is to create a simple version of the Blackjack game using Python.
Use the hints and structure below to guide you in building the game.

Objective:
You and the computer both draw cards from a deck. The goal is to have the highest hand without going over 21. 
Aces can be counted as 11 or 1, and face cards are all worth 10.
"""

############### Hints and Structure #####################

# Hint 1: Familiarize yourself with the game of Blackjack.
# Hint 2: Create functions for the different parts of the game logic.


# TODO: Use the function below as a starting point to deal a card:

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# TODO: Build on the function below to calculate the score of a hand:


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Add conditions for handling the Ace card
    # ... your code here ...

# Hint 3: Consider how you will structure the game loop.
# Hint 4: Implement game rules, e.g., if the player's score goes over 21, they lose.

# TODO: Create a function to compare scores of the player and the computer:


def compare(user_score, computer_score):
    # Implement conditions to determine the winner
    # ... your code here ...

    # Hint 5: Consider adding features like clearing the console and displaying a game logo.

    # TODO: Build the main function that drives the game:


def play_game():
    # Implement the game logic here
    # ... your code here ...

    # TODO: Create a loop to restart the game if the player wishes:
    # ... your code here ...
