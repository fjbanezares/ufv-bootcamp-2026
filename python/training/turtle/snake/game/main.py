from turtle import Screen
from snake import Snake  # Importing our previously defined, awesomely cool Snake class.
import time  # For suspense and drama! Just kidding, it's to control the speed of the game loop.

# Initialize the turtle screen. Think of this as laying down the canvas for our masterpiece.
screen = Screen()
screen.setup(
    width=600, height=600
)  # Sufficiently large playground for our snake. Size matters!
screen.bgcolor("black")  # Black, like the night! (Or an old-school arcade game.)
screen.title("My Snake Game")  # Titles are important, like naming your first-born.

# Disabling automatic screen updates. Why? For more control, and to prevent any flickering.
screen.tracer(0)

# Create a snake object. No, not a real snake! It's an instance of our Snake class!
snake = Snake()
# food = food()

# Keybindings setup using event listeners. Yes, listeners! They listen for your every command.
screen.listen()
# These are higher-order functions. Why? Because they accept functions (like snake.up) as arguments!
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Flag to control the game loop. True means the game is on, false will end the loop.
# Object state management 101: This is essentially the 'state' of our game!
game_is_on = True

# The heart of the game! Our game loop.
while game_is_on:
    # Update the screen first, before making any moves.
    screen.update()
    # Pause for a brief moment (0.1 sec). This sets the pace of our game. Too fast? Snake gets motion sickness.
    time.sleep(0.9)

    # Call the snake's move method to, well, move the snake!
    snake.move()

# Clean up after playing. Or else Mom will yell!
screen.exitonclick()
