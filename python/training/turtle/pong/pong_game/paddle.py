from turtle import (
    Turtle,
)  # Importing Turtle from the turtle module, a classic Python library for basic graphics.


# Defining the Paddle class, inheriting from the Turtle class.
# Basically, Paddle is a Turtle, but like, a more specific, paddle-shaped Turtle!
class Paddle(Turtle):
    # The magic starts here with our constructor method __init__!
    def __init__(self, position):
        super().__init__()  # Initializing the super class (Turtle), so we get all the Turtle methods and attributes.

        # Setting the paddle's shape. Square by default but, hey, we like to be explicit!
        self.shape("square")

        # What color should our paddle be? Milky white!
        self.color("white")

        # Changing the size of our paddle. We're stretching it! Like pre-workout but for a paddle.
        self.shapesize(stretch_wid=5, stretch_len=1)

        # We're lifting the pen up, we don't want to draw a line when our paddle moves!
        self.penup()

        # Going to the initial position specified when we create a Paddle object.
        # The paddle is like, "I gotta go, my people need me!" 🚀
        self.goto(position)

    # Go upwards, to infinity and beyond! Or, you know, just 20 units higher.
    def go_up(self):
        new_y = self.ycor() + 20  # Get the current y-coordinate and increase it by 20.
        self.goto(
            self.xcor(), new_y
        )  # Go to the new y-coordinate, while keeping x the same.

    # What goes up must come down. Physics 101 with our paddle. 📚
    def go_down(self):
        new_y = self.ycor() - 20  # Get the current y-coordinate and decrease it by 20.
        self.goto(
            self.xcor(), new_y
        )  # Go to the new y-coordinate, again keeping x the same.
