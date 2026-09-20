# Import the turtle module with the alias 't' for easier reference.
# Also import the random module, which will allow us to pick random colors and directions.
import turtle as t
import random

# Create a Turtle object named 'tim'.
# The Turtle object allows us to draw shapes by moving it around the screen.
tim = t.Turtle()

########### Challenge 4 - Random Walk ########

# What is a Random Walk?
# A random walk is a mathematical object that describes a path consisting of a succession of random steps.
# In our case, the turtle will choose a random direction and take a step, then choose another direction
# and take another step, and so on. Over time, this forms a "random walk" pattern.

# Create a list of colors to use for each step.
# These are simply color strings that the turtle module will understand.
colours = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]

# Create a list of possible directions that the turtle can move in.
# These are angles in degrees: 0 means forward, 90 means turn right, 180 means turn back, and 270 means turn left.
directions = [0, 45, 90, 135, 180, 225, 270, 315]

# Set the pen size to 15, making the line thicker for visibility.
tim.pensize(15)

# Set the turtle's speed to 'fastest' to make the drawing quicker.
# Note: This is optional and can be adjusted based on how fast you want the turtle to draw.
tim.speed("fastest")

# Loop 200 times to create 200 steps for our random walk.
for _ in range(400):
    # Randomly choose a color from the 'colours' list and set it as the turtle's pen color.
    tim.color(random.choice(colours))

    # Move the turtle forward by 30 units.
    tim.forward(15)

    # Randomly choose a direction from the 'directions' list and set it as the turtle's heading.
    # This will make the turtle face that direction for the next step.
    tim.setheading(random.choice(directions))
