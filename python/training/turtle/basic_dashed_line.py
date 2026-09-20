# Import the turtle module and alias it as 't' for easier reference.
# This way, every time we want to use a function from the turtle module, we can simply write 't' instead of 'turtle'.
# This is especially useful for modules with long names.
import turtle as t

# Create a Turtle object and name it 'tim'.
# This line initializes a turtle (a small arrow by default) that can move around the screen.
# We'll control this turtle to draw shapes.
tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########

# Loop 15 times to draw a dashed line.
# The for-loop will execute the indented block of code 15 times.
# Each dash will be drawn, followed by a space, 15 times in total.
for _ in range(15):
    # Move the turtle forward by 10 units while the pen is down.
    # This will draw a line as the turtle moves forward.
    tim.forward(10)

    # Lift the turtle's pen up from the canvas.
    # With the pen up, the turtle won't draw anything as it moves.
    # This is how we create the 'dash' effect, by lifting the pen up to create spaces between the lines.
    tim.penup()

    # Move the turtle forward by 10 units with the pen still up.
    # No line will be drawn in this step, creating the 'dash' in our dashed line.
    tim.forward(10)

    # Put the turtle's pen back down on the canvas.
    # Now the turtle is ready to draw again when it moves in the next iteration of the loop.
    tim.pendown()
