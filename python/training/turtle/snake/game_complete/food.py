from turtle import Turtle
import random


# Define a Food class that inherits from the Turtle class
class Food(Turtle):
    def __init__(self):
        # Initialize its parent class (Turtle)
        # We use super() to call the __init__ method of the parent class (Turtle)
        # This sets up all the turtle functionalities for our Food object
        super().__init__()

        # Set the shape of the Food as a circle
        # We use a circle as it's a simple shape and fits the game's aesthetics
        self.shape("circle")

        # Lift the pen up, so it doesn't draw anything when it moves
        # This is good for performance and avoids unnecessary lines on the screen
        self.penup()

        # Set the size of the Food object
        # stretch_len and stretch_wid of 0.5 make it smaller than the default size
        # to fit the design of our game
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)

        # Set the color of the Food object to blue
        # Blue contrasts well with the black background and white Snake
        self.color("blue")

        # Move the food to its initial position as quickly as possible
        # "fastest" makes sure it appears instantly
        self.speed("fastest")

        # Position the food at a random place on the screen
        # This calls the refresh method, discussed below
        self.refresh()

    def refresh(self):
        # Generate a random x and y coordinate for the Food object
        # We choose coordinates within (-280, 280) so it fits within our 600x600 screen
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)

        # Move the Food object to the new random position
        # goto() is inherited from the Turtle class
        self.goto(random_x, random_y)

        # The method ends here, and the Food object will have moved to a new position on the screen
