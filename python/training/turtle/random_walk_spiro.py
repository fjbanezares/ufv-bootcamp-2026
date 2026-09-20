# Import the turtle graphics library with the alias 't' to make it easier to type and read.
# Import the random library for generating random numbers.
import turtle as t
import random

# Create a Turtle object named 'tim' to control the turtle graphics.
tim = t.Turtle()

# Set the turtle graphics color mode to 255, enabling us to use RGB color values ranging from 0-255.
t.colormode(255)

tim.speed("fastest")


# Define a function to generate a random RGB color.
def random_color():
    r = random.randint(0, 255)  # Generate a random value for the red component.
    g = random.randint(0, 255)  # Generate a random value for the green component.
    b = random.randint(0, 255)  # Generate a random value for the blue component.
    color = (r, g, b)  # Create an RGB tuple.
    return color  # Return the generated random RGB color.


########### Challenge 5 - Spirograph ########

# What is a Spirograph?
# A spirograph is a geometric drawing that produces mathematical curves known as hypotrochoids and epitrochoids.
# Here, we'll be using turtle graphics to draw a spirograph by drawing circles with slight heading changes each time.


# Define a function to draw the spirograph.
def draw_spirograph(size_of_gap):
    # Loop to draw each circle in the spirograph.
    # 360 divided by the 'size_of_gap' gives us the number of circles needed to complete the spirograph.
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())  # Set the turtle pen color to a random color.
        tim.circle(100)  # Draw a circle with radius 100.

        # Change the heading (angle) of the turtle for the next circle.
        # This slight shift in angle is what gives us the spirograph pattern.
        tim.setheading(tim.heading() + size_of_gap)


# Call the function to start drawing the spirograph with a gap size of 5 degrees.
draw_spirograph(1)

t.done()
