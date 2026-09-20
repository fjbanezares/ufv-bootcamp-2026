# ####### Challenge 1 - Draw a Square ############
# Import the turtle module and give it an alias name 't' for easier referencing
import turtle as t

# Create a new turtle object called 'timmy_the_turtle'
# This creates a new turtle named Timmy, who will follow our drawing commands.
timmy_the_turtle = t.Turtle()

# Initialize a loop that will run 4 times (once for each side of the square)
# Using the underscore (_) as a variable name indicates that we don't plan to use it within the loop.
# It's just a way to run the indented block of code 4 times.
for _ in range(4):
    # Move the turtle 100 units forward to draw one side of the square
    # 'forward(100)' tells Timmy to move forward by 100 units, drawing a line as he moves.
    timmy_the_turtle.forward(100)

    # Turn the turtle 90 degrees to the left to get ready for the next side
    # 'left(90)' rotates Timmy 90 degrees to the left so that he's facing in the direction for the next line.
    timmy_the_turtle.left(90)

# At the end of the loop, we'll have a square on the screen.
