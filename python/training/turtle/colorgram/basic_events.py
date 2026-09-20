import turtle

# Create a turtle
t = turtle.Turtle()
screen = turtle.Screen()


# Function to move the turtle forward
def move_forward():
    t.forward(20)


# Function to turn the turtle left
def turn_left():
    t.left(45)


# Function to turn the turtle right
def turn_right():
    t.right(45)


# Function to exit the turtle window
def close():
    screen.bye()


# Register the callbacks for specific keys
# These are examples of higher-order functions
screen.onkey(move_forward, "w")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(close, "q")

# Listen for events
screen.listen()

# Keep the turtle window open
turtle.done()
