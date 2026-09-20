import turtle
import time

# Setup screen
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Turtle Clock")

# Draw clock face
face = turtle.Turtle()
face.penup()
face.goto(0, -210)
face.pendown()
face.pensize(5)
face.circle(210)

# Create a turtle for the hour hand
hour_hand = turtle.Turtle()
hour_hand.shape("arrow")
hour_hand.color("blue")
hour_hand.shapesize(stretch_wid=0.4, stretch_len=14)

# Create a turtle for the minute hand
minute_hand = turtle.Turtle()
minute_hand.shape("arrow")
minute_hand.color("red")
minute_hand.shapesize(stretch_wid=0.4, stretch_len=18)

# Create a turtle for the second hand
second_hand = turtle.Turtle()
second_hand.shape("arrow")
second_hand.color("green")
second_hand.shapesize(stretch_wid=0.4, stretch_len=20)


# Function to update the hands
def update_clock():
    while True:
        # Get the current local time
        current_time = time.localtime(time.time())

        # Calculate the angles for each hand
        hour = (current_time.tm_hour % 12) + current_time.tm_min / 60
        hour_angle = 90 - (hour * 360 / 12)
        minute_angle = 90 - (current_time.tm_min * 360 / 60)
        second_angle = 90 - (current_time.tm_sec * 360 / 60)

        # Update the turtles' angles
        hour_hand.setheading(hour_angle)
        minute_hand.setheading(minute_angle)
        second_hand.setheading(second_angle)

        # Wait for a bit before the next update
        time.sleep(1)
        second_hand.setheading(90)  # Reset second hand to avoid drawing a line


# Hide default turtle
turtle.hideturtle()

# Update clock
update_clock()

# To keep the window open
turtle.done()
