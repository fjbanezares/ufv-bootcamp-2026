import turtle
import time

s = turtle.getscreen()

t = turtle.Turtle()


t.right(90)
t.forward(100)
t.left(90)
t.backward(100)

# move to specific position
t.goto(100, 100)

# move to home similar to t.goto(0,0).
t.home()


# shape square
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)


# draw a circle
t.circle(60)
time.sleep(0.4)

# draw a dot
t.dot(50)
time.sleep(0.4)

# https://docs.python.org/3/library/turtle.html#turtle.color
turtle.bgcolor("blue")
time.sleep(0.4)
turtle.title("My Turtle Program")
time.sleep(0.4)


"""The numbers given are the parameters for the size of the turtle:

Stretch length
Stretch width
Outline width

"""
t.shapesize(1, 5, 10)
time.sleep(0.3)
t.shapesize(10, 5, 1)
time.sleep(0.3)
t.shapesize(1, 10, 5)
time.sleep(0.3)
t.shapesize(10, 1, 5)

# to increase and decrease the size of the pen
t.pensize(5)
t.forward(100)
time.sleep(0.5)

# Changing the Turtle and Pen Color
t.shapesize(3, 3, 3)
t.fillcolor("red")
t.forward(100)
time.sleep(0.5)
t.pencolor("green")
t.forward(100)
time.sleep(0.5)

t.home()
t.color("green", "red")
t.forward(100)
time.sleep(0.5)


# Filling in an Image
t.home()
t.begin_fill()
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
time.sleep(0.5)
t.end_fill()
time.sleep(0.5)

# turtle shape
"""
You have a couple of other options that you can try as well:

Square
Arrow
Circle
Turtle
Triangle
Classic

"""
t.shape("turtle")
time.sleep(0.5)
t.shape("arrow")
time.sleep(0.5)
t.shape("circle")
time.sleep(0.5)


# Changing the Pen Speed from 0 (the slowest speed) to 10 (the highest speed).
t.speed(1)
t.forward(200)
time.sleep(0.5)

t.speed(10)
t.forward(200)
time.sleep(0.5)

# excercise one line
t.home()
t.pencolor("purple")
t.fillcolor("orange")
t.pensize(10)
t.speed(9)
t.begin_fill()
t.circle(90)
t.end_fill()
t.forward(200)
time.sleep(0.5)

# pen in one line
t.pen(pencolor="purple", fillcolor="orange", pensize=10, speed=9)
t.begin_fill()
t.circle(90)
t.end_fill()
t.forward(200)
time.sleep(0.5)

# Undoing Changes
t.undo()
time.sleep(0.5)

# Clearing the Screen
t.clear()
t.forward(200)
time.sleep(0.5)

# Resetting the Environment
t.reset()
t.forward(200)
time.sleep(0.5)

# Leaving a Stamp
t.reset()

# Lista para almacenar los IDs de los stamps
stamp_ids = []
stamp_id = t.stamp()
stamp_ids.append(stamp_id)
t.fd(100)
stamp_id = t.stamp()
stamp_ids.append(stamp_id)
print(stamp_ids)
t.fd(100)
time.sleep(0.5)


t.clearstamp(stamp_ids[0])  # will clear the one with the stamp ID of 8.
time.sleep(0.5)

# Cloning Your Turtle
c = t.clone()
t.color("magenta")
c.color("red")
t.circle(100)
c.circle(60)
time.sleep(0.5)

# for Loops

# Create a square without a loop
t.reset()

t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)

time.sleep(0.5)

# Create a square with a loop
t.reset()

for i in range(4):
    t.fd(100)
    t.rt(90)

print(i)
time.sleep(0.5)


# while Loops

t.reset()

n = 10
while n <= 40:
    t.circle(n)
    n = n + 10

print(n)
time.sleep(0.5)

# Conditional Statements
t.reset()

u = input("Would you like me to draw a shape? Type yes or no: ")
if u == "yes":
    t.circle(50)
time.sleep(0.5)

# with elif and else
t.reset()

u = input("Would you like me to draw a shape? Type yes or no: ")
if u == "yes":
    t.circle(50)
elif u == "no":
    print("Okay")
else:
    print("Invalid Reply")

time.sleep(0.5)


# Keep the window open until it's manually closed.
turtle.done()
