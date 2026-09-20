# The challenge involves creating a bidding system.
# HINT: Think about how you can use dictionaries to solve this problem.

# Import the required modules. These modules are provided to you.
from art import logo
import os


def clear():
    # Using os.system() to execute the clear command specific to the operating system.
    os.system('cls' if os.name == 'nt' else 'clear')

    # DOS and Windows('nt'): Microsoft's DOS had the cls command to clear the screen. Windows, which initially started as a graphical layer over DOS, maintained a lot of command-line compatibility with DOS for ease of transition and backward compatibility. So, when Windows NT(New Technology) came about, it kept the cls command for clearing the screen.
    # Unix and Unix-like Systems: Unix is an OS that dates back to the 1970s. The command-line interface for Unix used the clear command. Many modern OSes, including Linux and macOS, are derived or inspired by Unix, so they keep the clear command for compatibility and tradition.


# Start by printing the provided logo.
print(logo)

# Create a dictionary to hold the bids.

# TODO: Set an initial state for the bidding process.

# TODO: Create a function to determine the highest bidder.


def find_highest_bidder(bidding_record):
    # Initialize the necessary variables to determine the winner.

    # Loop through the dictionary to determine the highest bid.

    # Print out the highest bidder.

    # TODO: Use a loop to continue receiving bids until there are no more bidders.

    # Remember to clear the console after each bid to keep the current bid private.
