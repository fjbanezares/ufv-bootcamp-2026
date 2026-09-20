# Welcome to the Python Snake Game Challenge!
# I've prepared a fun and educational challenge for you!
# I believe in your potential; let's dive into this adventure together. 😊

import time
import random
from turtle import Screen, Turtle


# -------------- SNAKE CLASS --------------
# The class that will define how our snake behaves.
class Snake:
    def __init__(self):
        self.segments = (
            []
        )  # The snake starts as a list of segments. Each segment is a Turtle object.
        self.create_snake()  # Call this method to create the initial snake.

    def create_snake(self):
        # Your challenge: Create the initial segments of the snake here!
        # Hint: Use a for loop and call the 'add_segment' method.
        pass

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # ... Your other methods for moving, extending, and changing directions go here ...


# -------------- FOOD CLASS --------------
# Ah, the Food class! You know, even a virtual snake has got to eat! 🍏
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # Challenge: Make the food appear at a random position on the screen.
        pass


# -------------- SCOREBOARD CLASS --------------
# Let's keep track of that high score, shall we? 🏆
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0  # Everybody starts somewhere, right?
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        # Challenge: Update the scoreboard with the current score.
        pass


# -------------- MAIN PROGRAM --------------
# Here is where the magic happens. 🌟
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turns off animation for instant screen updates.

# Create our Snake, Food, and Scoreboard objects.
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Challenge: Set up the keyboard listeners to control the snake.
# ...

# Let's start the game loop!
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # Challenge: Make the snake move!
    # ...

    # Challenge: Detect collision with food and increase the score.
    # ...

    # Challenge: Detect collision with wall and end the game.
    # ...

    # Challenge: Detect collision with tail and end the game.
    # ...

# And we're done! 🎉
# Once you've filled in the challenges, run the program to play your very own Snake game.
# Can't wait to see your awesome project!
