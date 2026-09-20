# This function calculates the number of cans needed to paint a wall, given the wall's height, width, and paint coverage.
# The formula is simple: Area of Wall / Coverage of Paint per Can.
# We will round up the result since we can't have a fraction of a paint can.
def paint_calc(height, width, cover):
    """
    Calculate the number of paint cans needed.

    Parameters:
    - height (int): The height of the wall.
    - width (int): The width of the wall.
    - cover (int): The coverage of the paint (how much area can be painted with a single can).

    Returns:
    None: It just prints the result.
    """

    # Calculate the area of the wall.
    area = height * width

    # Determine the number of cans needed.
    # The '//' operator in Python performs integer (floor) division, rounding down the result to the nearest whole number.
    # We add 1 to the result if there's a remainder to ensure we have enough paint,
    # because even if only a fraction of a can's worth of paint is needed, we still need an entire can.
    num_cans = area // cover + (area % cover > 0)

    # Display the result to the user.
    print(f"You'll need {num_cans} cans of paint.")


# User inputs for the height and width of the wall.
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))

# The coverage of the paint per can. It's given that one can covers 5 square meters.
coverage = 5

# Call the function with user inputs and the provided coverage.
paint_calc(height=test_h, width=test_w, cover=coverage)
