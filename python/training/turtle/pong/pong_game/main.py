# Import required modules. `turtle` is used for the graphical elements, while `time` controls the speed of the game loop.
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Initialize screen. This sets the stage where all the graphical elements will be displayed.
screen = Screen()
screen.bgcolor(
    "black"
)  # Background color set to black for better visibility of white paddles and ball.
screen.setup(width=800, height=600)  # Define the dimensions of the game window.
screen.title("Pong")  # Title to be displayed at the top of the game window.
screen.tracer(
    0
)  # Disables automatic screen updates, providing control over when the screen redraws.

# Initialize game elements.
r_paddle = Paddle((350, 0))  # Paddle on the right side of the screen.
l_paddle = Paddle((-350, 0))  # Paddle on the left side of the screen.
ball = Ball()  # Initialize ball in the center of the screen.
scoreboard = Scoreboard()  # Initialize scoreboard to keep track of scores.

# Event handling.
# `listen` makes the screen receptive to key events.
screen.listen()
# Bind keypress events to respective paddle movements. Uses lambda functions to pass methods.
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Main game loop. This is where the game state updates continuously.
game_is_on = True
while game_is_on:
    screen.update()  # Manually update screen elements.
    time.sleep(
        ball.move_speed
    )  # Pause loop for a short duration to make the ball's movement visible.
    ball.move()  # Invokes the move method on ball to update its position.

    # Collision detection with top and bottom walls.
    # Inverts vertical direction if the ball hits the top or bottom edge of the screen.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision detection with paddles.
    # Inverts horizontal direction if the ball comes into contact with either of the paddles.
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    # Scoring Logic
    # Update left score if the ball passes beyond the right paddle.
    if ball.xcor() > 380:
        ball.reset_position()  # Resets the ball's position to the center of the screen.
        scoreboard.l_point()  # Update left paddle's score.

    # Update right score if the ball passes beyond the left paddle.
    if ball.xcor() < -380:
        ball.reset_position()  # Resets the ball's position to the center of the screen.
        scoreboard.r_point()  # Update right paddle's score.

# Allows for manual window closure via mouse click.
screen.exitonclick()
