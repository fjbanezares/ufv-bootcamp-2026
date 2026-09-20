# Importing our dependable Turtle from turtle module 🐢
from turtle import Turtle

# Constants - They're like the North Star, never changing and guiding us.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial segments' positions
MOVE_DISTANCE = 20  # How far does the snake move in one go
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0  # Cardinal directions, no compass needed!


# Welcome to the Snake Kingdom 🐍
class Snake:
    # The constructor - where life begins.
    def __init__(self):
        self.segments = []  # Empty list to keep all our snake segments
        self.create_snake()  # Create that slithery boi
        self.head = self.segments[0]  # The head of the snake is the first segment

    # The snake builder! 🛠️
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)  # Create each segment at the given position

    # "The Segmentor" - Adds a segment to the snake 📏
    def add_segment(self, position):
        new_segment = Turtle("square")  # Square segments because we're hip to be square
        new_segment.color("white")  # White as snow ❄️
        new_segment.penup()  # No drawing on the move!
        new_segment.goto(
            position
        )  # To infinity and beyond! Or just to the given position...
        self.segments.append(new_segment)  # Add this segment to our segments list

    # The snake's growin' up so fast 😢
    def extend(self):
        self.add_segment(self.segments[-1].position())  # Add a segment at the end

    # "Move it, move it!" 🎵
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # Move from tail to head
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)  # The new position of the segment
        self.head.forward(MOVE_DISTANCE)  # Move the head forward

    # Head turns UP ☝️
    def up(self):
        if self.head.heading() != DOWN:  # Can't go back on yourself, silly snake!
            self.head.setheading(UP)

    # Head turns DOWN 👇
    def down(self):
        if self.head.heading() != UP:  # No U-turns!
            self.head.setheading(DOWN)

    # Head turns LEFT 👈
    def left(self):
        if self.head.heading() != RIGHT:  # Lefty loosey!
            self.head.setheading(LEFT)

    # Head turns RIGHT 👉
    def right(self):
        if self.head.heading() != LEFT:  # Righty tighty!
            self.head.setheading(RIGHT)

    # New beginnings! 🔄
    # Reset the snake for a new game
    def reset(self):
        for segment in self.segments:  # Send all segments out of sight
            segment.goto(1000, 1000)
        self.segments.clear()  # Empty the segments list
        self.create_snake()  # Create a new snake
        self.head = self.segments[0]  # Reset the head
