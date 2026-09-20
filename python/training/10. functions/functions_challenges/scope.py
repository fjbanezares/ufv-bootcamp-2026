################### Scope ####################

# Global variable `enemies` defined in the global scope
enemies = 1

# A function that has its own local scope


def increase_enemies():
    # This is a local variable with the same name as the global variable.
    # It's defined within the function's scope and does not affect the global variable.
    enemies = 2
    print(f"enemies inside function: {enemies}")


# Calling the function will print the local `enemies` value
increase_enemies()
# This will print the global `enemies` value
print(f"enemies outside function: {enemies}")

# The function `drink_potion` has a local variable `potion_strength`


def drink_potion():
    potion_strength = 2
    print(potion_strength)


# Calling the function prints the local `potion_strength`
drink_potion()
# This will raise an error because `potion_strength` is not defined in the global scope
# print(potion_strength)  # Uncommenting this line will cause an error

# Global variable `player_health`
player_health = 10

# A function `game` that contains another function `drink_potion`


def game():
    # Nested function
    def drink_potion():
        # This function accesses the global variable `player_health`
        potion_strength = 2
        print(player_health)
    # Calling the nested function within `game`
    drink_potion()


# This will print the global `player_health` value
print(player_health)

# Global variable `game_level`
game_level = 3

# Function demonstrating that Python does not have block-level scope


def create_enemy():
    # Local list of enemies
    enemies = ["Skeleton", "Zombie", "Alien"]
    # The variable `new_enemy` is defined inside an if block
    if game_level < 5:
        new_enemy = enemies[0]
    # Even though `new_enemy` is defined inside an if block, it's accessible in the entire function's scope
    print(new_enemy)

# This function is used to demonstrate the best way to modify a global variable from within a function


def increase_enemies():
    # Access the global `enemies` variable
    print(f"enemies inside function: {enemies}")
    # Instead of modifying it directly, we return the modified value
    return enemies + 1


# Reassign the global `enemies` variable to the value returned from the function
enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Defining global constants
# By convention, global constants are written in uppercase
PI = 3.1415926
URL = "https://www.google.com"
TWITTER_HANDLE = "@fjbanezares"
