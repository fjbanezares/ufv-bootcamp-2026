# Import the turtle module.
# Note: The turtle module itself is a singleton.
# That means all subsequent imports of this module will refer to the same object.
import turtle

# Create the first turtle object.
# Each call to turtle.Turtle() creates a new, distinct instance of the Turtle class.
first_turtle = turtle.Turtle()
first_turtle.color("blue")  # Set the color of the first turtle to blue.

# Move the first turtle to a starting position.
first_turtle.penup()
first_turtle.goto(-100, 0)
first_turtle.pendown()

# Draw a square with the first turtle.
for _ in range(4):
    first_turtle.forward(100)
    first_turtle.left(90)

# Create the second turtle object.
# Again, this is a new, distinct instance, separate from the first_turtle object.
second_turtle = turtle.Turtle()
second_turtle.color("red")  # Set the color of the second turtle to red.

# Move the second turtle to a starting position.
second_turtle.penup()
second_turtle.goto(100, 0)
second_turtle.pendown()

# Draw a triangle with the second turtle.
for _ in range(3):
    second_turtle.forward(100)
    second_turtle.left(120)

# Despite coming from the same imported module, first_turtle and second_turtle
# are separate instances and can be manipulated independently.

# Keep the window open until it's manually closed.
turtle.done()
