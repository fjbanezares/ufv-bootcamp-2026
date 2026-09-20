import time  # We use this to slow down our game loop
from turtle import Screen  # A turtle Screen object to set up our game window
from player import (
    Player,
)  # Our player class that represents the turtle crossing the road
from car_manager import CarManager  # Our car manager that handles all car-related logic
from scoreboard import Scoreboard  # The scoreboard to keep track of the player's level

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(
    0
)  # Stops automatic screen updates, we'll do it manually for more control

# Initialize our player, car manager and scoreboard
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Listen for keypress events
screen.listen()
screen.onkey(player.go_up, "Up")  # When "Up" key is pressed, turtle moves up

# The main game loop
game_is_on = True
while game_is_on:  # This loop will continue to run as long as game_is_on is True
    # time.sleep(0.1)  # Pause for 0.1 seconds; gives us a chance to see what's happening
    screen.update()  # Manually update the screen

    car_manager.create_car()  # Try to create a car (it has a 1/6 chance each loop iteration)
    car_manager.move_cars()  # Move all existing cars

    # Collision detection with car
    for car in car_manager.all_cars:  # Iterate over all existing cars
        if (
            car.distance(player) < 20
        ):  # Turtle's collision detection method, if < 20 it's a collision
            game_is_on = False  # End the game
            scoreboard.game_over()  # Display "Game Over"

    # Check for successful crossing
    if player.is_at_finish_line():  # If player's y-coordinate is past a certain point
        player.go_to_start()  # Send the player back to the start
        car_manager.level_up()  # Increase the car speed
        scoreboard.increase_level()  # Increase the level on the scoreboard

    # Alternative Methods:
    # 1) We could have implemented a pause and resume feature using a different game state variable.
    # 2) Collision could have been pixel-perfect for more realism but may be computationally intensive.
    # 3) A state machine could be implemented for various game states like 'playing', 'paused', 'game_over'.
    # 4) Sounds or music could be added for more interaction.
    # 5) The level-up mechanics could be more complex, like adding more cars or introducing obstacles.

screen.exitonclick()  # Exits the game when the screen is clicked
