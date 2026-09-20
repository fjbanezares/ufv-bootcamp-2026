# TODO: Import required modules
from game_data import data  # Import game data
# TODO: Import other necessary modules here

# TODO: Define a function that returns a random account from 'data'


def get_random_account():
    # Your code here
    pass

# TODO: Define a function that formats account data for display


def format_data(account):
    # Your code here
    pass

# TODO: Define a function to check if the user's guess is correct


def check_answer(guess, a_followers, b_followers):
    # Your code here
    pass

# Main function to run the game


def game():
    print(logo)  # Display the game's logo

    score = 0  # Initialize the score
    game_should_continue = True  # Initialize game loop control variable

    # TODO: Get two random accounts
    account_a = get_random_account()
    account_b = get_random_account()

    # TODO: Main game loop. Complete the loop that runs the game.
    while game_should_continue:
        # Your code here

        # TODO: Make sure that account_a and account_b are not the same. If they are, get a new account for account_b.

        # Your code here

        # TODO: Display the accounts for comparison (use the format_data function)

        # Your code here

        # TODO: Get the user's guess on who has more followers ('A' or 'B')

        # Your code here

        # TODO: Extract follower counts from both accounts for comparison

        # Your code here

        # TODO: Check if the user's guess is correct (use the check_answer function)

        # Your code here

        # TODO: Clear the screen

        # Your code here

        # Display the logo again
        print(logo)

        # TODO: Update the score or end the game based on the user's guess

        # Your code here

# TODO: Start the game by calling the game function
