# Let's start by explaining the basic concept of scope with an easy example.
# In Python, variables have different lifetimes and visibility depending on where they are defined.
# Please follow along and understand how Python deals with different levels of variable scopes. Thank you!

# Global Scope - This variable is accessible from anywhere in the file
global_var = "I am global!"  # Thanks for defining me in the global scope! I'm visible everywhere.

# This is a built-in function. Built-in scope includes things Python has predefined, such as `print`.
print(global_var)  # Output: "I am global!"


# Now, let's introduce Local Scope. This is where variables are only visible inside a function or method.
def my_function():
    # This is a local variable, defined inside the function
    local_var = "I live inside a function!"
    print(local_var)  # You can access me here, inside the function.

my_function()  # Output: "I live inside a function!"
# If you try to print `local_var` outside the function, it will result in an error:
# print(local_var)  # Error! `local_var` is not defined here.


# Let's look at the Enclosing scope with nested functions. Thank you for your patience as we go deeper!

def outer_function():
    enclosing_var = "I live in the outer function."  # This is in the enclosing scope.

    def inner_function():
        # Inner function can access `enclosing_var` because it's in the enclosing scope.
        print(enclosing_var)  # Thank you for allowing me to access the enclosing scope variable!

    inner_function()  # Calling the inner function.

outer_function()  # Output: "I live in the outer function."

# Note: If you try to access `enclosing_var` outside of `outer_function`, it won't work:
# print(enclosing_var)  # Error! This variable is in the enclosing scope, so it's not accessible here.

# Now let's play with the concept of Global scope inside a function
def another_function():
    global global_var  # We use `global` to modify the global variable inside the function.
    global_var = "I have been changed globally!"  # Changing the global variable from within the function.
    print(global_var)  # Output: "I have been changed globally!" 

another_function()
print(global_var)  # Output: "I have been changed globally!"


# Now let's introduce how to return functions from within functions and access enclosing variables. Thanks for sticking around!

def outer_with_return():
    x = 10  # Enclosing scope variable

    def inner_return(y):
        return x + y  # Accessing the enclosing scope variable

    return inner_return  # Returning the inner function itself, not its result

add_to_ten = outer_with_return()  # This assigns `inner_return` to `add_to_ten`
print(add_to_ten(5))  # Output: 15 (because 10 (enclosing scope) + 5 = 15)


# Time to play with nested scopes and variable shadowing. Please pay attention to how the names behave! Thanks!

x = "global x"

def outer():
    x = "outer x"  # This shadows the global `x`

    def inner():
        nonlocal x  # This keyword allows us to modify the enclosing scope's `x`
        x = "inner x"  # This changes `x` in the outer function's scope.
        print(x)  # Output: "inner x" (Thanks for letting me change the enclosing variable!)

    inner()
    print(x)  # Output: "inner x" because we changed the outer function's `x`.

outer()
print(x)  # Output: "global x" (Global `x` remains unchanged)

# Let's finish with an exercise about using built-ins! Python gives us access to built-in names in the global scope.
# You don’t have to import or define these functions – thanks Python! Examples include `print()`, `len()`, `str()`, etc.

my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Built-in `len` function. Output: 5

# If we try to shadow built-ins, things might get confusing. Let's demonstrate with a harmless example.
len = "I am a string now, not a function!"  # Oops! We just shadowed the built-in `len()`.
print(len)  # Output: "I am a string now, not a function!"

# Now, if we try to use the `len` function again, it will raise an error because we replaced it with a string.

# print(len(my_list))  # Error! `len` is no longer a function.

# Pro tip: Avoid shadowing built-ins, please! Thanks for being cautious.

# Time to reset `len` to its original built-in function.
del len  # Now `len()` is back to being the built-in function.
print(len(my_list))  # Output: 5 (Thank you for not shadowing built-ins anymore!)

# That's a wrap! This example code explained:

# 1. Local Scope (inside functions)

# 2. Enclosing Scope (nested functions)

# 3. Global Scope (accessible throughout the file)

# 4. Built-in Scope (always available functions and constants)

# Thanks for following along! You're now well-versed in Python's LEGB rule. :)