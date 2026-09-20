from turtle import Screen, Turtle
import time

# Define initial settings for the snake
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# Snake class: Model our snake buddy
class Snake:
    def __init__(self):
        # Initialize an empty list to keep all the snake segments
        self.segments = []
        # Call the function to create initial snake segments
        self.create_snake()
        # The first segment is the head of the snake
        self.head = self.segments[0]

    def create_snake(self):
        # Loop through the STARTING_POSITIONS list and create a turtle at each position
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
        # Your Challenge: Can you refactor this function to avoid repetition?

    # Your Challenge: Implement the 'move' function to move the snake forward
    def move(self):
        pass  # Remove this pass statement and write your code here

    # Implement turning functions (Hint: set the heading)
    # Your Challenge: Complete these functions to turn the snake
    def up(self):
        pass

    def down(self):
        pass

    def left(self):
        pass

    def right(self):
        pass


# Main game logic starts here
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turns off animation for instant screen update

snake = Snake()  # Create a Snake object

# Register keyboard events
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# The game loop: the beating heart of the game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()  # Your Challenge: Implement the snake movement

# To close the window when clicked
screen.exitonclick()
