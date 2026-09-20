from turtle import (
    Turtle,
)  # The unsung hero of Python's standard library for graphical stuff.


# The Ball class inherits from the Turtle class, 'cause why reinvent the wheel (or in this case, the ball)?
class Ball(Turtle):
    # The constructor to end all constructors. (Well, not really, but it's important!)
    def __init__(self):
        super().__init__()  # Calling the superclass constructor, classic move!
        self.color("white")  # No disco ball here, just a plain white circle.
        self.shape("circle")  # Making sure our ball is, well, a ball.
        self.penup()  # No trails, Hansel and Gretel.

        # The x_move and y_move decide the ball's direction. Positive numbers only. We're optimists.
        self.x_move = 3
        self.y_move = 3

        # The speedster attribute. Starting slow, like your first coffee in the morning.
        self.move_speed = 0.01

    # The move method, because a ball's gotta roll.
    def move(self):
        new_x = self.xcor() + self.x_move  # Calculate new x-coordinate.
        new_y = self.ycor() + self.y_move  # Calculate new y-coordinate.
        self.goto(new_x, new_y)  # Onwards, to glory!

    # A bounce in the y-direction is just negating the y_move. It's like saying, "I change my mind!"
    def bounce_y(self):
        self.y_move *= -1

    # When bouncing in x-direction, let's make it zippier by 10%. Exciting stuff!
    def bounce_x(self):
        self.x_move *= -1  # Flip the x direction.
        self.move_speed *= 0.05  # Getting faster, like it just saw a spider.

    # Resets ball to the center, aka its "happy place."
    def reset_position(self):
        self.goto(0, 0)  # Taking the ball back to its home.
        self.move_speed = 0.005  # Reset the speed. Phew, take a breather!
        self.bounce_x()  # Flipping x direction as a polite way to say, "your turn!"
