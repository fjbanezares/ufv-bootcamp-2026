# Importing the required function and variable
from random import randint
from art import logo

# Defining constants for the maximum turns for each difficulty level
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check if the user's guess is correct


def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

# Function to set the difficulty level of the game


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# Main game function


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # Choosing a random number between 1 and 100 as the answer
    answer = randint(1, 100)
    # This line is for debugging and should be removed in the final version
    print(f"Pssst, the correct answer is {answer}")

    # Setting the difficulty and getting the number of turns
    turns = set_difficulty()

    # Initializing user's guess
    guess = 0

    # Game loop continues until user's guess is correct or turns run out
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Getting user's guess
        guess = int(input("Make a guess: "))

        # Checking the user's guess and updating the number of turns left
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            # Using 'return' without arguments to gracefully exit the game function.
            # This ends the current game session without proceeding further.
            # This approach helps in controlling the flow of the program without
            # adding additional nested conditions or breaking loops. It makes the code cleaner and more readable.
            return
        elif guess != answer:
            print("Guess again.")


# Starting the game
game()
