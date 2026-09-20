# Let's start with a basic example to explain `global` and `nonlocal` keywords.
# Please follow the comments carefully for better understanding. Thanks!

x = 10  # Global variable

def outer_function():
    # This is the outer function
    y = 20  # Enclosing variable (Enclosing scope)
    
    def inner_function():
        # This is the inner function
        z = 30  # Local variable
        print(f"Inside inner_function: x = {x}, y = {y}, z = {z}")
        # It can access global and enclosing variables as well.
    
    inner_function()
    print(f"Inside outer_function: x = {x}, y = {y}")
    # This function cannot access `z` because `z` is local to `inner_function`.

outer_function()
print(f"Global scope: x = {x}")
# Output shows how local, enclosing, and global variables work.

# Please note: Python resolves variable scope using LEGB rule:
# L: Local
# E: Enclosing
# G: Global
# B: Built-in

print("\n---Example 1: Using global keyword---\n")

def use_global():
    global x  # Please note we are declaring `x` as global.
    print(f"Before modification: x = {x}")
    x = 50  # This modifies the global variable.
    print(f"After modification: x = {x}")

use_global()
print(f"Global scope after modification: x = {x}")
# `global` allows modifying the global variable directly from inside the function. Thanks!

print("\n---Example 2: Using nonlocal keyword---\n")

def outer_nonlocal():
    y = 30  # Enclosing variable

    def inner_nonlocal():
        nonlocal y  # Please note `y` is marked as nonlocal.
        print(f"Before nonlocal modification: y = {y}")
        y = 40  # This modifies `y` in the enclosing scope.
        print(f"After nonlocal modification: y = {y}")

    inner_nonlocal()
    print(f"Inside outer_nonlocal: y = {y}")
    # `y` was modified in the inner function thanks to the nonlocal keyword.

outer_nonlocal()

# Now, let's explore a more complex case:
print("\n---Example 3: Difference between global and nonlocal---\n")

x = 100  # Global variable again

def outer_mixed():
    x = 200  # Enclosing variable
    
    def inner_mixed():
        global x  # Declaring global x
        print(f"Global x before modification in inner_mixed: {x}")
        x = 300  # Modifying the global variable
        print(f"Global x after modification in inner_mixed: {x}")
    
    inner_mixed()
    print(f"Inside outer_mixed: x = {x} (Enclosing scope didn't change)")
    # The global variable changed, but the enclosing variable remains the same.

outer_mixed()
print(f"Global scope after inner_mixed: x = {x}")
# This demonstrates the distinction between modifying global and enclosing scope.

print("\n---Example 4: When nonlocal and global interact---\n")

# Nonlocal cannot modify global variables, but let's demonstrate this interaction.

x = 10  # Global variable

def outer_interaction():
    x = 20  # Enclosing variable
    
    def inner_interaction():
        nonlocal x  # This modifies the enclosing `x`, not the global one.
        print(f"Before nonlocal modification: x = {x}")
        x = 30
        print(f"After nonlocal modification: x = {x}")
    
    inner_interaction()
    print(f"Inside outer_interaction: x = {x}")
    # The enclosing variable `x` was modified.

outer_interaction()
print(f"Global x remains unchanged: x = {x}")
# Please note the global variable didn't change; only the enclosing one did.

print("\n---Example 5: What happens if no enclosing variable exists?---\n")

#def no_enclosing():
  #  def inner_no_enclosing():
 #       nonlocal x  # Trying to use nonlocal when there's no enclosing x
       # x = 5  # This will cause a SyntaxError because there's no enclosing variable.
   # inner_no_enclosing()

# Uncomment the next line to see the SyntaxError:
# no_enclosing()

# If you run the above code, it will raise:
# SyntaxError: no binding for nonlocal 'x' found
# Please don't forget to comment it out after testing. Thanks!

print("\n---Example 6: Global vs Nonlocal with the same name---\n")

# What happens when the global and enclosing variables have the same name?

x = 5  # Global variable

def outer_same_name():
    x = 10  # Enclosing variable
    
    def inner_same_name():
        nonlocal x  # Refers to enclosing x, not the global one.
        print(f"Before nonlocal modification: x = {x}")
        x = 15  # Modifies the enclosing `x`
        print(f"After nonlocal modification: x = {x}")
    
    inner_same_name()
    print(f"Inside outer_same_name: x = {x}")  # Enclosing variable modified.

outer_same_name()
print(f"Global x remains unchanged: x = {x}")
# Please note that nonlocal modifies the enclosing variable even if it shares the same name with global.

# That's it! Hope you find the global and nonlocal keywords much clearer now.
# Thanks for reading and experimenting!
