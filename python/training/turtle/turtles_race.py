# Turtle Racing Game - A race you can bet on, without leaving your shell 🐢💨

from turtle import Turtle, Screen  # Importing the VIPs: Turtle and Screen!
import random  # Because who doesn't love surprises?

# Let's set the mood! The race doesn't start until we say so! 🚦
is_race_on = False

# Pop up the screen, it's showtime! 🖥️
screen = Screen()
screen.setup(width=500, height=400)  # Roomy enough for a thrilling race!

# Time to bet! Place your bets, folks! No refunds! 🎰
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)

# Our racing champions are ready! 🌈
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# Yes, they've all got their lanes. No pushing!
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []  # This will be the VIP lounge for our racing turtles.

# Roll out the turtles! 🐢🐢🐢🐢🐢🐢
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()  # No graffiti artists here!
    new_turtle.color(colors[turtle_index])  # Dress to impress!
    new_turtle.goto(x=-230, y=y_positions[turtle_index])  # On your marks!
    all_turtles.append(new_turtle)  # Welcome to the VIP lounge!

# No bet, no race! Life's tough, huh? 😜
if user_bet:
    is_race_on = True

# Ready, Set, GO! 🏁
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:  # Who's crossing the finish line?
            is_race_on = False  # Stop the press!
            winning_color = (
                turtle.pencolor()
            )  # The color function in the Turtle library sets both the pencolor
            # and the fillcolor at the same time. That's why the turtle and the pen color are the same in this example. It's like hitting two birds—or should I say turtles?—with one stone!
            # Why did the turtle use the same color for drawing and its shell? Because it wanted to be a "well-coordinated" artist! 🐢🎨
            if winning_color == user_bet:  # Did you win?
                print(f"You've won! The {winning_color} turtle is the winner! 🥳")
            else:  # Better luck next time!
                print(f"You've lost! The {winning_color} turtle is the winner! 😭")

        # And they're off! 🐢💨
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Don't rush off! Click to exit. 🖱️
screen.exitonclick()
