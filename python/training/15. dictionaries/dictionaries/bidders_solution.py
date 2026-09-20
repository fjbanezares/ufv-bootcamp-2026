# Importing the 'os' module to access the operating system and perform a screen clear.
import os
# Importing the logo from the 'art' module to display at the beginning.
from art import logo

# Function to clear the terminal screen.


def clear():
    # Using os.system() to execute the clear command specific to the operating system.
    os.system('cls' if os.name == 'nt' else 'clear')


# Printing the logo to the terminal.
print(logo)

# Initializing an empty dictionary to hold the bids.
bids = {}
# Setting an initial state for the bidding process.
bidding_finished = False

# Function to determine the highest bidder.


def find_highest_bidder(bidding_record):
    # Initializing a variable to store the highest bid found.
    highest_bid = 0
    
    # Initializing a variable to store the name of the highest bidder.
    winner = ""
    
    # Iterating through the bidding_record dictionary.
    # By default, when you iterate over a dictionary, it gives you the keys (the bidders in this case).
    for bidder in bidding_record:
        # Accessing the bid amount using the key (bidder).
        # bidder is the key, and bidding_record[bidder] gives you the value (the bid amount).
        bid_amount = bidding_record[bidder]
        
        # Check if the current bid is higher than the current highest bid.
        if bid_amount > highest_bid:
            # If the current bid is higher, update the highest_bid to this new higher value.
            highest_bid = bid_amount
            
            # Also, update the winner to be the current bidder (the key from the dictionary).
            winner = bidder
    # Printing the winner and their bid amount to the terminal.
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    print(f"This should be hidden but {bidding_record}")


# While loop to continue taking bids until there are no more bidders.
while not bidding_finished:

    clear()
    print(logo)

    # Prompt the user for their name.
    name = input("What is your name?: ")
    # Prompt the user for their bid amount and convert it to an integer.
    price = int(input("What is your bid?: $"))
    # Store the bid in the 'bids' dictionary with the bidder's name as the key.
    bids[name] = price
    # Ask if there are any other bidders.
    should_continue = input(
        "Are there any other bidders? Type 'yes or 'no'.\n")
    # Check the user's response.
    if should_continue == "no":
        # If 'no', set 'bidding_finished' to True to end the while loop.
        bidding_finished = True
        # Call the function to find and print the highest bidder.
        find_highest_bidder(bids)
    # If the user says there are other bidders, clear the terminal for the next bidder.
    # elif should_continue == "yes":
     #   clear()
