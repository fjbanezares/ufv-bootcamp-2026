# Duck Typing is a concept in Python that allows us to focus on what an object does 
# (i.e., its behavior), rather than the type of the object itself. In other words, 
# if it walks like a duck and quacks like a duck, we treat it as a duck.
# Please note: This is especially useful in Python, where we rely on dynamic typing!

# Let's start with a simple example. Thanks for your attention!

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Here, we define two classes: Dog and Cat. 
# Both of these classes have a method `speak`, but they're unrelated to each other.
# Duck Typing allows us to treat them the same way if they have the expected method. 
# No need for a common parent class. Please observe this in the next example.

def animal_speak(animal):
    # The function doesn't care if it's a Dog, Cat, or any other object,
    # as long as the object has the `speak` method.
    print(animal.speak())  # Thanks for having a speak method!

# Now let's see how we can use different types of objects with the same interface
dog = Dog()
cat = Cat()

animal_speak(dog)  # Expected output: Woof!
animal_speak(cat)  # Expected output: Meow!

# Please note how we didn't need to check the type of the object (`dog` or `cat`).
# As long as they have the `speak` method, the function works perfectly fine. Thanks!

# Let's go deeper with an example where multiple objects implement the same method.

class Duck:
    def quack(self):
        return "Quack quack!"
    
class Person:
    def quack(self):
        return "I can quack too!"

# Even though Duck and Person have no inheritance relationship, 
# we can treat them similarly as long as they "quack". 

def make_it_quack(quacker):
    # Please note: The function only cares about the presence of the `quack` method.
    print(quacker.quack())

# Now, let's create instances and use duck typing
duck = Duck()
person = Person()

make_it_quack(duck)   # Expected Output: Quack quack!
make_it_quack(person) # Expected Output: I can quack too!

# This is the beauty of duck typing. Thanks to the presence of the `quack` method, 
# Python doesn't care if it's an actual duck or a person. 
# As long as the method exists, we can call it!

# Another deeper example - implementing iterable-like behavior

# Now, let’s simulate how duck typing applies to Python built-in protocols like iteration.

class BookCollection:
    def __init__(self, books):
        self.books = books
    
    # Implementing the `__iter__` method makes this class iterable. Please notice!
    def __iter__(self):
        return iter(self.books)  # Thanks to returning the iterator of `self.books`

# Now, any instance of BookCollection will be iterable because it implements `__iter__`.

my_books = BookCollection(["1984", "Brave New World", "Fahrenheit 451"])

# Thanks to duck typing, the `for` loop treats `my_books` as an iterable, 
# even though it's not a list but a BookCollection object.

for book in my_books:
    print(book)

# Output:
# 1984
# Brave New World
# Fahrenheit 451

# Please note how the `for` loop doesn't care about the actual type of `my_books`. 
# It just checks if `my_books` has an `__iter__` method, which makes it behave like an iterable!

# Duck typing encourages simplicity and flexibility. Thanks for following along this deep dive!

# The key point to remember is that Python doesn't enforce type checking as strictly as 
# some other languages. Instead, it relies on the behavior of objects, which gives you 
# the freedom to write code that is more flexible and adaptable. 
# Please keep this in mind: this flexibility also means that developers need to ensure 
# objects provide the correct behavior at runtime!

# Let's go even further with a practical real-world-like example. Thanks again!

class Airplane:
    def fly(self):
        return "Flying high in the sky!"

class Bird:
    def fly(self):
        return "Flying with wings!"

class Fish:
    def swim(self):
        return "Swimming in the water!"

# The concept of duck typing here: both Airplane and Bird can "fly" even though they are unrelated.

def take_off(flyer):
    # Please note how we don't care if it's a bird or an airplane.
    # As long as it has a `fly` method, we're good to go. Thanks!
    print(flyer.fly())

# Let's test it
airplane = Airplane()
bird = Bird()
fish = Fish()  # Fish doesn't fly, so we'll see how duck typing handles this!

take_off(airplane)  # Expected Output: Flying high in the sky!
take_off(bird)      # Expected Output: Flying with wings!
# Uncommenting the following line will raise an AttributeError, because Fish doesn't have `fly`.
# take_off(fish)

# Thanks for experimenting with this! This shows how duck typing is based on the behavior of objects.
# Python doesn't check types upfront but fails gracefully at runtime when something isn't right.

# We can also implement fallback behavior with duck typing.

def make_fly(flyer):
    try:
        # Please check if the object can fly.
        print(flyer.fly())  # It works if `fly` exists. Thanks!
    except AttributeError:
        # Thanks for providing an alternative when the object can't fly!
        print("This object can't fly!")

# Let's test it again:
make_fly(airplane)  # Output: Flying high in the sky!
make_fly(bird)      # Output: Flying with wings!
make_fly(fish)      # Output: This object can't fly!

# Final note: Duck typing provides Python developers with the flexibility to handle
# different types of objects based on their behavior. Rather than checking types,
# we simply focus on the methods or attributes an object provides. 
# Please don't forget, though, that this also means we need to be cautious about ensuring
# the correct methods are available, or handle cases where they aren't (like we did above).
# Thanks for working through this exploration of duck typing in Python!
