# Import the turtle module with the alias 't' for easier reference.
# Also import the random module, which will allow us to pick random colors.
import turtle as t
import random

# Create a Turtle object named 'tim'.
# The Turtle object allows us to draw shapes by moving it around the screen.
tim = t.Turtle()

# Set the speed of the turtle to 1, which is the slowest speed.
# This will make it easier to observe the turtle as it draws.
tim.speed(2)

# Set the pen size to 3, for a thicker line.
# This will make the lines more visible.
tim.pensize(4)

########### Challenge 3 - Draw Shapes ########

# Create a list of colors to use for the shapes.
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
    "pink",
    "black",
]


# Define a function called 'draw_shape' that takes an argument 'num_sides'.
# This function will draw a regular polygon with 'num_sides' number of sides.
def draw_shape(num_sides):
    # Calculate the angle to turn at each corner of the shape.
    # For a regular polygon, the sum of all interior angles is 360 degrees.
    angle = 360 / num_sides

    # Loop 'num_sides' times to draw each side of the shape.
    for _ in range(num_sides):
        # Move the turtle forward by 100 units.
        tim.forward(100)

        # Turn the turtle to the right by the calculated angle.
        # This prepares the turtle for drawing the next side of the shape.
        tim.right(angle)


# Loop through numbers from 3 to 9, each representing the number of sides for a shape.
# We start from 3 because a shape with fewer than 3 sides doesn't make sense.
for shape_side_n in range(3, 12):
    # Pick a random color from the 'colours' list and set the turtle's pen to that color.
    tim.color(random.choice(colours))

    # Call the 'draw_shape' function to draw a shape with 'shape_side_n' number of sides.
    # This will draw a series of regular polygons starting from a triangle (3 sides) up to a nonagon (9 sides).
    draw_shape(shape_side_n)

# This will keep the Turtle graphics window open until you close it manually.
t.done()
