from turtle import Turtle

# Woo-hoo! Constants! They make life so much easier and your code more readable.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 30
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# Welcome to the Snake class! Your one-stop shop for creating slithering digital pets.
class Snake:
    # Initiation ritual for our snake. Let's get this party started! 🎉
    def __init__(self):
        self.segments = (
            []
        )  # A list to keep all our snake segments. Think of it as the snake's spine!
        self.create_snake()  # Build that snake! Construct it segment by segment.
        self.head = self.segments[
            0
        ]  # The head leads the way. No one likes a headless snake, right?

    # Create the initial snake. It's like the blueprint for our reptilian friend.
    def create_snake(self):
        for (
            position
        ) in STARTING_POSITIONS:  # Looping through starting positions like a pro.
            new_segment = Turtle(
                "turtle"
            )  # Squares are the new circles, didn't you know?
            new_segment.color(
                "white"
            )  # Why white? Because it's the color of purity... and our snake is a good snake.
            new_segment.penup()  # No ink trails here! Our snake is clean and discreet.
            new_segment.goto(position)  # To the starting positions, march!
            self.segments.append(
                new_segment
            )  # Adding to the body. The snake is getting longer!

    # Let's get moving! Slither time! 🐍
    def move(self):
        # We start from the tail, allowing each segment to catch up to its neighbor. Like a conga line!
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # The head takes the lead! Someone has to do it!
        self.head.forward(MOVE_DISTANCE)

    # Turning time! Show off those dance moves! 💃
    def up(self):
        if self.head.heading() != DOWN:  # No U-turns! This snake follows the law!
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:  # Can't pull a Michael Jackson moonwalk here!
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:  # Left is always right, except when it's not!
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:  # Right on! Let's make that turn!
            self.head.setheading(RIGHT)


# And there we have it! A snake that can not only move but also groove! 🎶
