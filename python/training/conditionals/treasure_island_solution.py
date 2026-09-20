# ASCII art to give a visual introduction to the game.
print('''
*******************************************************************************
          |                   |                  |                     |
...
... [the rest of the ASCII art]
...
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# The game starts with the first choice at the crossroad.
choice1 = input(
    'You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()

# If the user chooses 'left', the game progresses to the next stage.
if choice1 == "left":
    # Now the user encounters a lake.
    choice2 = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()

    # If the user decides to wait, they progress to the next stage.
    if choice2 == "wait":
        # Now the user is presented with three doors.
        choice3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose? \n").lower()

        # Each door has its own outcome.
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            # In case the user chooses something other than the given door colors.
            print("You chose a door that doesn't exist. Game Over.")

    # If the user decides to swim, an unfavorable outcome awaits.
    else:
        print("You get attacked by an angry trout. Game Over.")

# If the user chooses 'right' at the first choice, the game ends.
else:
    print("You fell into a hole. Game Over.")
