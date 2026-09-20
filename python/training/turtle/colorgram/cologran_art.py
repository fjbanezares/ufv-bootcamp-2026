# Importing the turtle module and renaming it as turtle_module for further reference.
# Importing random module to generate random numbers for color choices.
import turtle as turtle_module
import random

# Setting the turtle module's color mode to 255, which allows us to use RGB color codes.
turtle_module.colormode(255)

# Creating a turtle object named 'tim'.
tim = turtle_module.Turtle()

# Setting the speed of 'tim' to the fastest.
tim.speed("fastest")

# Lifting up the pen so that 'tim' won't draw lines when moving.
tim.penup()

# Hiding the turtle object on the screen.
tim.hideturtle()

# A predefined list of RGB tuples, each representing a color.
color_list = [
    (224, 154, 102),
    (152, 76, 53),
    (60, 33, 28),
    (36, 24, 29),
    (236, 210, 166),
    (235, 195, 134),
    (108, 44, 34),
    (195, 103, 72),
    (20, 18, 26),
    (107, 74, 80),
    (91, 48, 52),
    (238, 176, 150),
    (80, 77, 97),
    (202, 119, 48),
    (189, 136, 146),
    (178, 99, 109),
    (232, 202, 209),
    (62, 59, 77),
    (227, 171, 181),
    (143, 137, 157),
    (127, 118, 145),
    (23, 26, 24),
    (218, 214, 228),
    (100, 58, 23),
]

# Setting the initial direction of the turtle to 225 degrees.
tim.setheading(225)

# Moving the turtle forward by 300 units.
tim.forward(300)

# Setting the turtle's direction back to 0 degrees (East).
tim.setheading(0)

# Defining the total number of dots that the turtle will draw.
number_of_dots = 100

# Loop to draw each dot.
# The variable dot_count keeps track of the number of dots drawn so far.
for dot_count in range(1, number_of_dots + 1):
    # 'tim' puts a dot on the screen. The size of the dot is 20, and the color is randomly chosen from color_list.
    tim.dot(20, random.choice(color_list))

    # 'tim' moves forward by 50 units to prepare for drawing the next dot.
    tim.forward(50)

    # If 10 dots have been drawn, it's time to move to the next line.
    # The check "dot_count % 10 == 0" ensures this.
    if dot_count % 10 == 0:
        # Turn the turtle 90 degrees (North) to go to the next line.
        tim.setheading(90)

        # Move forward 50 units.
        tim.forward(50)

        # Turn 180 degrees to point West.
        tim.setheading(180)

        # Move forward 500 units to go back to the starting position of this line.
        tim.forward(500)

        # Turn back to the initial direction (East).
        tim.setheading(0)

# This line initializes the screen where the turtle operates.
screen = turtle_module.Screen()

# Save the screen content to a PostScript file
canvas = turtle_module.getcanvas()
canvas.postscript(file="turtle_art.eps")

# The screen will close when clicked.
screen.exitonclick()
