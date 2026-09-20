# Importing required modules
# Imports 'data', which is a list of dictionaries containing the game's data.
from game_data import data
import random  # Required to randomize the selection of accounts.
from art import logo, vs  # Imports ASCII art to beautify the display.
from os import system  # Importing 'system' from 'os' to clear the screen.

# Define a function to get a random account from the list 'data'.


def get_random_account():
    # Picks and returns a random dictionary (account) from the list 'data'.
    return random.choice(data)

# Define a function to format an account's data for display.


def format_data(account):
    # Extracts individual attributes from the dictionary for easier reference.
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # Returns the formatted string.
    return f"{name}, a {description}, from {country}"

# Define a function to check if the user's guess is correct.


def check_answer(guess, a_followers, b_followers):
    # Compare follower counts between two accounts and return whether the user's guess matches.
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Define the main game function.


def game():
    print(logo)  # Prints the game's logo at the start.
    score = 0  # Initialize the score to zero.
    game_should_continue = True  # Control variable for the game loop.

    # Initialize two random accounts for the first round.
    account_a = get_random_account()
    account_b = get_random_account()

    # Main game loop.
    while game_should_continue:
        # Move the previous 'account_b' to 'account_a' for the next round.
        account_a = account_b
        # Get a new random 'account_b' for the next round.
        account_b = get_random_account()

        # Make sure both accounts are not the same.
        while account_a == account_b:
            account_b = get_random_account()

        # Display formatted account information.
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)  # Print the versus symbol.
        print(f"Against B: {format_data(account_b)}.")

        # Get the user's guess.
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Extract the follower counts for comparison.
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        # Check if the user's guess was correct.
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        # Clear the terminal screen.
        system('clear')

        # Display the logo again.
        print(logo)

        # Check the guess and update the score or end the game.
        if is_correct:
            score += 1  # Increment the score.
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False  # End the game.
            print(f"Sorry, that's wrong. Final score: {score}")


# Start the game.
game()
