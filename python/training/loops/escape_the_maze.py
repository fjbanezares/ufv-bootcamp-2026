

# this makes the day
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if (front_is_clear() and wall_on_right()):
        move()
    elif (front_is_clear() and not wall_on_right()):
        turn_right()
        move()
    elif (not front_is_clear() and wall_on_right()):
        turn_left()
    elif (not front_is_clear() and not wall_on_right()):
        turn_right()
        move()

    else:
        turn_right()

else not needed as all possibilities are considered


def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if (front_is_clear() and wall_on_right()):
        move()
    elif (not front_is_clear() and wall_on_right()):
        turn_left()
    elif (front_is_clear() and not wall_on_right()):
        turn_right()
        move()
        if (front_is_clear() and not wall_on_right()):
            turn_right()
            move()


while not at_goal():
     if (front_is_clear() and wall_on_right()):
          move()
      elif (front_is_clear() and not wall_on_right()):
        turn_right()
        move()
      elif (not front_is_clear() and wall_on_right()):
        turn_left()
      elif (not front_is_clear()):
        turn_right()
        move()

      else:
          turn_right()
