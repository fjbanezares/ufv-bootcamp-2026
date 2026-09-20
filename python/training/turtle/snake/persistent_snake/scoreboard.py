from turtle import Turtle

# Constants for aligning the text and setting the font
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


# The Scoreboard class inherits from the Turtle class
class Scoreboard(Turtle):
    # The constructor (__init__) initializes the Scoreboard instance
    def __init__(self):
        super().__init__()  # Initialize the superclass (Turtle)

        self.score = 0  # Initialize the current score to zero

        # Use 'with' for context management to ensure the file is properly closed after reading
        # This reads the high score from the "data.txt" file and stores it
        with open("data.txt") as data:
            self.high_score = int(
                data.read()
            )  # Convert string read from the file to an integer

        self.color("white")  # Set the color of the text to white
        self.penup()  # Lift the pen to prevent drawing when moving
        self.goto(0, 270)  # Position the turtle to display the score
        self.hideturtle()  # Hide the turtle object on screen
        self.update_scoreboard()  # Update the scoreboard initially

    # This method updates the score and high score display
    def update_scoreboard(self):
        self.clear()  # Clears previous score so that new score can be written
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )  # Display new score and high score

    # Reset the game while keeping track of the high score
    def reset(self):
        # Check if a new high score is achieved
        if self.score > self.high_score:
            self.high_score = self.score  # Update the high score

            # Persist the new high score by writing it to the "data.txt" file
            # Use 'with' to ensure that the file is properly closed after writing
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")  # Write the new high score as a string

        self.score = 0  # Reset current score to zero for a new game
        self.update_scoreboard()  # Update the scoreboard after reset

    # Increase the score by 1
    def increase_score(self):
        self.score += 1  # Increment the current score
        self.update_scoreboard()  # Update the scoreboard to show the new score
