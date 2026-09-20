from turtle import Turtle

# Initialize starting positions for the snake segments and other constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20  # Distance each segment moves in a single step
UP = 90  # Angle representing UP direction
DOWN = 270  # Angle representing DOWN direction
LEFT = 180  # Angle representing LEFT direction
RIGHT = 0  # Angle representing RIGHT direction


# Snake class definition
class Snake:
    # Initialize the snake by creating its segments
    def __init__(self):
        self.segments = []  # Store individual snake segments as turtle objects
        self.create_snake()  # Create the initial snake
        self.head = self.segments[0]  # The first segment is the head of the snake

    # Method to create a snake with segments at the starting positions
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # Method to create a new segment at a specific position
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # Extend the snake by adding a segment at the last segment's position
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Method to move the snake forward
    def move(self):
        # Start from the last segment moving it to the position of its preceding segment
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # Move the head forward by MOVE_DISTANCE units
        self.head.forward(MOVE_DISTANCE)

    # Methods to change the snake's direction
    def up(self):
        if (
            self.head.heading() != DOWN
        ):  # Prevents the snake from moving in the opposite direction
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(2000, 2000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]  # The first segment is the head of the snake
