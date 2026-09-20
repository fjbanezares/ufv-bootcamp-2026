# Importing the turtle module
import turtle

# Initialize the turtle window
wn = turtle.Screen()
wn.title("Distance Between Turtles")

# Create a turtle named 'alice'
alice = turtle.Turtle()
alice.shape("turtle")
alice.color("blue")

# Create another turtle named 'bob'
bob = turtle.Turtle()
bob.shape("turtle")
bob.color("red")

# Move 'alice' to a position
alice.goto(0, 0)
alice.dot(20, "blue")

# We'll calculate distance in several ways

# Case 1: Calculate distance from 'alice' home (0,0) to a specific coordinate (30, 40)
# home() method moves the turtle to the origin (0,0)
alice.home()
# distance(x, y) calculates the distance from the turtle's current position to (x,y)
distance_to_point = alice.distance(30, 40)
print(f"Distance from Alice to (30, 40): {distance_to_point}")

# Case 2: Calculate distance using a tuple for coordinates
# We can also pass a tuple to the distance method
distance_to_point = alice.distance((30, 40))
print(f"Distance from Alice to (30, 40) using tuple: {distance_to_point}")

# Case 3: Calculate distance from 'alice' to 'bob'
# First, let's move 'bob' to a position
bob.goto(30, 40)
bob.dot(20, "red")
# Now, we calculate the distance from 'alice' to 'bob'
distance_to_bob = alice.distance(bob)
print(f"Distance from Alice to Bob: {distance_to_bob}")

# Using distance() for another turtle
# Create a third turtle named 'joe'
joe = turtle.Turtle()
joe.shape("turtle")
joe.color("green")
# Move 'joe' forward by 77 units
joe.forward(77)
joe.dot(20, "green")
# Calculate distance from 'alice' to 'joe'
distance_to_joe = alice.distance(joe)
print(f"Distance from Alice to Joe: {distance_to_joe}")

# To keep the window open until user closes it
wn.mainloop()
