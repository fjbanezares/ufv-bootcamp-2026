# Time to keep score! 🎯
# We're importing our good ol' friend, Turtle!
from turtle import Turtle

# Constants to keep the code clean. 🧼
# Font and alignment details, so you don't have to remember it each time.
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


# Behold, the Scoreboard class! 🏆
# Inherits all the turtle goodness from Turtle class.
class Scoreboard(Turtle):
    # The constructor of destiny! 🌈
    def __init__(self):
        super().__init__()  # "I got it from my daddy!" 🎶 Inherit everything from parent class.
        self.score = 0  # We're all zeroes when we're born, right? 🐣
        self.color("white")  # The ink for our invisible pen. 🖋
        self.penup()  # Lift the pen up, we're just moving here, not drawing!
        self.goto(0, 270)  # Go to the top of the screen, young Turtle!
        self.hideturtle()  # We're like the John Cena of turtles, invisible! 🤫
        self.update_scoreboard()  # The first score to be displayed will be 0.

    # Update Scoreboard 🔄
    # Refresh the score display.
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # The End is Nigh! ☠️
    # Show the 'GAME OVER' text.
    def game_over(self):
        self.goto(0, 0)  # Go to the center of the universe.
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)  # Write the sad truth.

    # Level Up! ⬆️
    # Increase the score when the snake eats food.
    def increase_score(self):
        self.score += 1  # Ah ah ah! 🧛‍♂️
        self.clear()  # Out with the old!
        self.update_scoreboard()  # In with the new!

    # The Phoenix rises! 🐦🔥
    # Reset the score to 0 for a new game.
    def reset(self):
        # self.score = 0  # Back to square one, baby!
        self.clear()  # Clean slate.
        # self.update_scoreboard()  # Start afresh!
        self.__init__()
