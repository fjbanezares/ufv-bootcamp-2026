from turtle import (
    Turtle,
)  # Importing the Turtle class from the turtle library for graphics.


# The Scoreboard class inherits from the Turtle class, a stellar example of object-oriented programming.
class Scoreboard(Turtle):
    # Constructor method initializes the instance of the Scoreboard.
    def __init__(self):
        super().__init__()  # Invoke the constructor of the parent class (Turtle).
        self.color(
            "white"
        )  # Set the text color to white, great for visibility on a dark background.
        self.penup()  # Lifts the pen to ensure the turtle object doesn't draw anything.
        self.hideturtle()  # We don't want to see the turtle object, just the text it writes.

        # Initialize left and right scores. It's like tennis but for turtles.
        self.l_score = 0
        self.r_score = 0

        self.update_scoreboard()  # Initial display of the scoreboard.

    # Method to update the scoreboard on the screen.
    def update_scoreboard(self):
        self.clear()  # Clear any previous score. Clean slate, new opportunities!

        # Writing the left score.
        self.goto(-100, 200)  # Positioning turtle to the left upper quadrant.
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))

        # Writing the right score.
        self.goto(100, 200)  # Positioning turtle to the right upper quadrant.
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    # Method to increase the left score and update the scoreboard.
    def l_point(self):
        self.l_score += 1  # Incrementing the left score.
        self.update_scoreboard()  # Refreshing the scoreboard with the new score.

    # Method to increase the right score and update the scoreboard.
    def r_point(self):
        self.r_score += 1  # Incrementing the right score.
        self.update_scoreboard()  # Again, refreshing the scoreboard with the updated score.
