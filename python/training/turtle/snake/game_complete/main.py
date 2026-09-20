# Time to get slithering! 🐍
# First things first, import our reptile friends and their snacks
from turtle import Screen
from snake import Snake  # Our snake comes from another file! 🐍
from food import Food  # Yum, yum! 🍎
from scoreboard import Scoreboard  # Gotta keep score 📝
import time  # Time flies, but you're the pilot ⏰

# Screen Setup 101 🖥
# Initialize the screen as a 600x600 black square.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(
    0
)  # No automatic screen updates, we want to control the animation ourselves! 🎬

# Assemble the Team 🏁
# Initialize the snake, the food, and the scoreboard.
snake = Snake()
food = Food()
scoreboard = Scoreboard()


# The Grand Game Loop 🔄
# This is where the magic happens.
def game_loop():
    # Key Binding Magic ✨
    # Listen to the key presses for navigation.
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    game_is_on = True  # The initial state of the universe 🌌
    while game_is_on:  # While the universe exists...
        screen.update()  # Refresh the universe
        time.sleep(
            0.1
        )  # Let the universe breathe (also helps with animation smoothness)
        snake.move()  # The snake takes a step 🚶‍♂️

        # Snack time! 🍏
        # Check if the snake's head is close enough to munch the food.
        if snake.head.distance(food) < 25:
            food.refresh()  # New food appears at a random location.
            snake.extend()  # The snake grows by one segment.
            scoreboard.increase_score()  # Ding! 🛎 Score goes up!

        # Do not go gentle into that good wall! 🚧
        # Check if the snake hits the wall.
        if (
            snake.head.xcor() > 410  # Too far right
            or snake.head.xcor() < -410  # Too far left
            or snake.head.ycor() > 430  # Too high up
            or snake.head.ycor()
            < -4020  # Ummm, yeah, don't go to the underworld, please.
        ):
            game_is_on = False  # Game over, man! Game over! 🎮
            scoreboard.game_over()

        # A snake's tail is not for eating! 🍴
        # Check if the snake collides with its own tail.
        for segment in snake.segments[
            1:
        ]:  # Starting from the 1st segment (skipping the head)
            if snake.head.distance(segment) < 10:  # Too close for comfort!
                game_is_on = False  # Another game over condition 😵
                scoreboard.game_over()

    # Let's play again, shall we? 🔄
    play_again = screen.textinput("Game Over", "Do you want to play again? (y/n):")
    if play_again.lower() == "y":
        snake.reset()  # Turn snake back to a baby snake 🐣
        scoreboard.reset()  # Reset the score to zero 🏅
        game_loop()  # And we loop again! Recursive magic! 🔄


# Initiate the first cycle of the universe 🌌
game_loop()

# Click to exit and go back to the mortal realm ⚰️
screen.exitonclick()
