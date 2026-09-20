# Simple demonstration of how nonlocal affects only the nearest enclosing variable `x`
# Let's start with a function `outer` that has several nested functions.
# Each function will have its own variable `x`, and we will see how nonlocal affects only the closest one.

def outer():
    x = "outer x"  # This is `x` in the outermost function

    def mid():
        x = "mid x"  # This is `x` in the middle function
        
        def inner():
            nonlocal x  # Refers to `x` in mid, the nearest enclosing function
            x = "modified mid x"  # Changes `x` in mid, not in outer
            print(f"In inner: x = {x}")
            # At this point, `x` from mid has been modified, not `x` from outer.

        inner()  # Call inner function to modify `x` in mid
        print(f"In mid after inner: x = {x}")
        # After calling inner, `x` in mid has been changed, but `x` in outer is unaffected.

    mid()  # Call mid function, which calls inner
    print(f"In outer after mid: x = {x}")
    # `x` in outer remains unchanged.

# Let's run the outer function and see the output
outer()

# Now let's make it even clearer by adding another layer.
# This time, we'll add an extra function `deeper` and see how nonlocal affects only the nearest `x`.
x = 3,1415
def outer_again():
    x = "outer_again x"  # `x` in the outermost function again

    def mid_again():
        global x
        x = "mid_again x"  # `x` in the middle function again
        
        def deeper():
            x = "deeper x"  # `x` in the deeper function (this one won't be affected by nonlocal)

            def inner_again():
                nonlocal x  # Refers to `x` in mid_again, NOT `x` in deeper
                x = "modified mid_again x"  # This changes `x` in mid_again
                print(f"In inner_again: x = {x}")
                # The nearest `x` (mid_again's) is changed, deeper's `x` is untouched.

            inner_again()  # Call inner_again to modify `x` in mid_again
            print(f"In deeper after inner_again: x = {x}")
            # `x` in deeper remains unchanged because nonlocal didn't reference it.

        deeper()  # Call deeper function, which calls inner_again
        print(f"In mid_again after deeper: x = {x}")
        # `x` in mid_again was changed by nonlocal in inner_again.

    mid_again()  # Call mid_again function, which calls deeper
    print(f"In outer_again after mid_again: x = {x}")
    # `x` in outer_again remains unchanged.

# Let's run the outer_again function
print("global before...",x)
outer_again()
print("global after...",x)

# What did we learn?
# - `nonlocal` only affects the nearest `x` in the enclosing scope, not all `x` variables at every level.
# - In this case, `x` in `mid` or `mid_again` is modified, while the outermost `x` remains unaffected.
# - The deepest `x` in the `deeper` function remains untouched by nonlocal, as it doesn't reference it.
# Thanks for following along!
