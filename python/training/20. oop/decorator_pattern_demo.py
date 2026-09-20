# Please and thanks for understanding this decorator pattern! 
# It's an elegant design that allows us to "decorate" objects by adding behavior dynamically!

# The main Circle class that we will decorate
class Circle:
    def __init__(self):
        self.radius = 5  # A basic attribute, thanks for paying attention!

    def draw(self):
        # Please note that this is the basic 'draw' method
        return "Drawing a circle"

# Now, we will create our first decorator, which adds color to the Circle
class ColorDecorator:
    def __init__(self, circle, color):
        # Thanks for passing the circle we are decorating!
        self.circle = circle  # This is our 'core' object
        self.color = color  # The new color attribute we're adding, please take note!

    def draw(self):
        # Please see how we call the original draw method and "wrap" it with new behavior
        return f"{self.circle.draw()} with color {self.color}"

# Here's another decorator! It adds thickness to the circle's outline
class ThicknessDecorator:
    def __init__(self, circle, thickness):
        # Again, we are wrapping the circle object, thank you for the circle object!
        self.circle = circle
        self.thickness = thickness  # The new thickness we will add, nice!

    def draw(self):
        # We use the original circle's draw method and modify the behavior. Thank you for your attention!
        return f"{self.circle.draw()} with thickness {self.thickness}px"

# Adding yet another decorator: Now we can add a pattern to the circle
class PatternDecorator:
    def __init__(self, circle, pattern):
        self.circle = circle  # Wrapping the circle object, thank you!
        self.pattern = pattern  # The pattern we're applying

    def draw(self):
        return f"{self.circle.draw()} with {self.pattern} pattern"

# Now let's create our Circle object first, please!
my_circle = Circle()

# We can now decorate this circle with a color, a thickness, and a pattern
my_colored_circle = ColorDecorator(my_circle, "red")
my_thick_circle = ThicknessDecorator(my_colored_circle, 10)  # Thank you for using multiple decorators!
my_pattern_circle = PatternDecorator(my_thick_circle, "striped")

# Now, when we draw, it will have multiple layers of behavior added.
# Thanks for running this! Look at the decorated circle!
print(my_pattern_circle.draw())
# Expected Output: Drawing a circle with color red with thickness 10px with striped pattern

# Here’s another example! We can create another circle and decorate it differently.
another_circle = Circle()
another_decorated_circle = ThicknessDecorator(another_circle, 5)
print(another_decorated_circle.draw())
# Expected Output: Drawing a circle with thickness 5px

# Decorators can be stacked dynamically, at runtime!
# This means you can flexibly compose new behaviors without modifying the original class!

# More features can be added easily by creating new decorators
class ShadowDecorator:
    def __init__(self, circle, shadow_size):
        self.circle = circle
        self.shadow_size = shadow_size  # Adding shadow size!

    def draw(self):
        return f"{self.circle.draw()} with shadow size {self.shadow_size}px"

# We can create a new decorated circle with shadow now
my_shadowed_circle = ShadowDecorator(my_thick_circle, 15)
print(my_shadowed_circle.draw())
# Expected Output: Drawing a circle with color red with thickness 10px with shadow size 15px

# Thanks for exploring the Decorator Pattern!
# Notice how we've composed multiple decorators together to modify behavior dynamically!

