import turtle

# Initialize screen
wn = turtle.Screen()
wn.title("Move Turtles and Calculate Distance")
wn.bgcolor("white")

# Create turtles: Alice and Bob
alice = turtle.Turtle()
alice.shape("turtle")
alice.color("blue")

bob = turtle.Turtle()
bob.shape("turtle")
bob.color("red")


# Function to move Alice
def move_alice(x, y):
    alice.goto(x, y)
    display_distance()


# Function to move Bob
def move_bob(x, y):
    bob.goto(x, y)
    display_distance()


# Function to calculate and display distance
def display_distance():
    distance = alice.distance(bob)
    alice.clear()
    bob.clear()
    alice.write(
        f"Distance to Bob: {distance:.2f}", align="center", font=("Arial", 12, "normal")
    )
    bob.write(
        f"Distance to Alice: {distance:.2f}",
        align="center",
        font=("Arial", 12, "normal"),
    )


# Bind turtles to mouse clicks
turtle.onscreenclick(move_alice, 1)  # Left mouse button to move Alice
turtle.onscreenclick(move_bob, 3)  # Right mouse button to move Bob

# Initialize with a distance display
display_distance()

# Keep the window open
turtle.done()
