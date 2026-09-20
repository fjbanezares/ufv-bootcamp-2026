# Challenge: Complete the Turtle Race!

from turtle import Turtle, Screen  # TODO: Import the necessary modules

# TODO: Initialize race conditions, like `is_race_on`

screen = Screen()  # TODO: Set up the screen with appropriate width and height

# TODO: Use the textinput method to get the user's bet

colors = ["red", "orange", "yellow", "green", "blue", "purple"]  # TODO: List of possible turtle colors
y_positions = [-70, -40, -10, 20, 50, 80]  # TODO: Starting y-positions for our racers
all_turtles = []  # TODO: Create an empty list to store all turtle objects

# TODO: Create the turtles and add them to the list of all_turtles
# Use a for loop and set their attributes like shape, color, etc.
# Place them at their starting positions

# TODO: Set the race flag based on whether the user placed a bet

# Ready, Set, Go!
while is_race_on:  # TODO: Start the race if is_race_on is True
    for turtle in all_turtles:
        # TODO: Move each turtle forward by a random amount and check if they've won the race.
        # If any turtle wins, set is_race_on to False and announce the winner.

# TODO: Add an exit condition for the screen

