# Import the turtle module
import turtle

# Create a new turtle screen and set its attributes
wn = turtle.Screen()
wn.title("My Turtle Example")
wn.bgcolor("lightgreen")

# Create a turtle named tommy
tommy = turtle.Turtle()
tommy.shape("turtle")  # set the shape attribute
tommy.color("blue")     # set the color attribute

# Create a turtle named timmy
timmy = turtle.Turtle()
timmy.shape("triangle")  # set the shape attribute
timmy.color("red")        # set the color attribute
timmy.penup()             # pick up the pen
timmy.goto(-100, 0)       # move to position (-100, 0)
timmy.pendown()           # put the pen down

# Use tommy to draw a square
for i in range(4):
    tommy.forward(100)
    tommy.right(90)

# Use timmy to draw a triangle
for i in range(3):
    timmy.forward(100)
    timmy.right(120)

# Hide the turtles
tommy.hideturtle()
timmy.hideturtle()

# Close the window when clicked
wn.mainloop()
