from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time  # Importing the time module to control the speed of the game loop

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off the screen updates for manual control

# Initialize our snake, food, and scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Event handling: listening for keyboard inputs
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()  # Manually update the screen
    time.sleep(0.1)  # Pause for a short time to slow down the snake
    snake.move()  # Move the snake forward

    # Collision detection with food
    if (
        snake.head.distance(food) < 15
    ):  # If the distance to the food is less than 15 pixels
        food.refresh()  # Move the food to a new random location
        snake.extend()  # Extend the snake
        scoreboard.increase_score()  # Increase the score

    # Collision detection with wall
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        scoreboard.reset()
        snake.reset()

    # Collision detection with tail
    for segment in snake.segments:
        if segment == snake.head:  # Skip the head segment
            pass
        elif (
            snake.head.distance(segment) < 10
        ):  # Check collision with the other segments
            scoreboard.reset()
            snake.reset()

# Allows you to click to close the game window
screen.exitonclick()
