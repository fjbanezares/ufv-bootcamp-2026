# Import the turtle library
import turtle

# Create a screen object
wn = turtle.Screen()
wn.title("Turtle Deep Dive Example")  # Set the title
wn.bgcolor("white")  # Set the background color

# Create a turtle named tommy
tommy = turtle.Turtle()
# Configure tommy
tommy.shape("turtle")  # Set the shape
tommy.color("green")  # Set the color
tommy.pensize(2)  # Set the pen size

# Draw a square with tommy
tommy.penup()  # Lift the pen up
tommy.goto(-50, 50)  # Move the turtle to x, y coordinate (-50, 50)
tommy.pendown()  # Put the pen down
for i in range(4):  # Loop to draw a square
    tommy.forward(100)  # Move forward 100 units
    tommy.right(90)  # Rotate 90 degrees to the right

# Create another turtle named timmy
timmy = turtle.Turtle()
# Configure timmy
timmy.shape("triangle")  # Set the shape
timmy.color("blue")  # Set the color
timmy.pensize(2)  # Set the pen size

# Draw a circle with timmy
timmy.penup()  # Lift the pen up
timmy.goto(50, -50)  # Move the turtle to x, y coordinate (50, -50)
timmy.pendown()  # Put the pen down
timmy.circle(50)  # Draw a circle with radius 50 units

# Use tommy to write text on screen
tommy.penup()
tommy.goto(-20, 0)  # Position to write text
tommy.write("Hello!", font=("Arial", 16, "normal"))  # Write the text

# Configure both turtles to move to initial positions
tommy.penup()
tommy.goto(-150, 0)
timmy.penup()
timmy.goto(150, 0)

# Use both turtles to draw parallel lines
for i in range(30):
    tommy.pendown()
    timmy.pendown()
    tommy.forward(5)
    timmy.forward(5)
    tommy.penup()
    timmy.penup()
    tommy.forward(5)
    timmy.forward(5)

# Hide turtlespip install --upgrade setuptools wheel

tommy.hideturtle()
timmy.hideturtle()

# Wait for user to close window
wn.mainloop()
