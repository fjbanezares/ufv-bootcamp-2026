# Thanks for joining this deep dive into multiple inheritance in Python!
# Please, let's start by creating some mixin classes for our demonstration.

# Mixin 1: WalkMixin
class WalkMixin:
    def walk(self):
        # This method will be used to walk.
        print(f"{self.__class__.__name__} is walking")  # Thanks for walking!

# Mixin 2: TalkMixin
class TalkMixin:
    def talk(self):
        # This method will be used to talk.
        print(f"{self.__class__.__name__} is talking")  # Thanks for talking!

# Mixin 3: EatMixin
class EatMixin:
    def eat(self):
        # This method will be used to eat.
        print(f"{self.__class__.__name__} is eating")  # Thanks for eating!

# Mixin 4: SleepMixin
class SleepMixin:
    def sleep(self):
        # This method will be used to sleep.
        print(f"{self.__class__.__name__} is sleeping")  # Thanks for sleeping!

# Now let's combine multiple mixins using multiple inheritance.
# The order of inheritance is important due to Python's MRO.

class Person(WalkMixin, TalkMixin, EatMixin, SleepMixin):
    def __init__(self, name):
        # The constructor method for the Person class.
        self.name = name  # Thanks for naming the person!

    def introduce(self):
        # Let's introduce the person with a special message.
        print(f"Hello, I am {self.name}")  # Thanks for introducing yourself!

# Let's create an object of the Person class and test the inherited methods.
p = Person("Alice")

# Calling methods from mixins (inherited behavior)
p.walk()  # Output: Alice is walking
p.talk()  # Output: Alice is talking
p.eat()   # Output: Alice is eating
p.sleep() # Output: Alice is sleeping

# Let's print the MRO (Method Resolution Order) to see how Python resolves method lookups.
print(Person.mro())
# Output:
# [<class '__main__.Person'>, <class '__main__.WalkMixin'>, 
# <class '__main__.TalkMixin'>, <class '__main__.EatMixin'>, 
# <class '__main__.SleepMixin'>, <class 'object'>]
# Thanks for checking the MRO!

# Now let's create a more complex example with method overlap and MRO behavior.

# Mixin 5: MoveMixin
class MoveMixin:
    def move(self):
        # This method is used to move.
        print(f"{self.__class__.__name__} is moving")  # Thanks for moving!

# Mixin 6: FastMoveMixin, inheriting MoveMixin
class FastMoveMixin(MoveMixin):
    def move(self):
        # This method overrides the move method from MoveMixin.
        print(f"{self.__class__.__name__} is moving fast!")  # Thanks for moving fast!

# Let's create a new class that inherits from both MoveMixin and FastMoveMixin
class SuperPerson(Person, FastMoveMixin):
    def fly(self):
        # This method is used to fly.
        print(f"{self.__class__.__name__} is flying")  # Thanks for flying!

# Create an object of the SuperPerson class
sp = SuperPerson("Super Alice")

# Calling methods from the multiple inherited classes
sp.walk()  # Output: Super Alice is walking
sp.talk()  # Output: Super Alice is talking
sp.eat()   # Output: Super Alice is eating
sp.sleep() # Output: Super Alice is sleeping
sp.fly()   # Output: Super Alice is flying
sp.move()  # Output: Super Alice is moving fast! (from FastMoveMixin)

# Let's print the MRO (Method Resolution Order) for SuperPerson class.
print(SuperPerson.mro())
# Output:
# [<class '__main__.SuperPerson'>, <class '__main__.Person'>, <class '__main__.WalkMixin'>, 
# <class '__main__.TalkMixin'>, <class '__main__.EatMixin'>, <class '__main__.SleepMixin'>, 
# <class '__main__.FastMoveMixin'>, <class '__main__.MoveMixin'>, <class 'object'>]
# Thanks for analyzing the MRO of SuperPerson!

# Now let's see how the MRO affects method resolution when there are overlaps.
# The method in FastMoveMixin is resolved before MoveMixin due to its higher priority in the MRO.

# Exercise: Try changing the order of inheritance in SuperPerson and see how the MRO changes!

# Example with Conflicting Methods: 
class A:
    def action(self):
        print("Action from A")

class B(A):
    def action(self):
        print("Action from B")

class C(A):
    def action(self):
        print("Action from C")

class D(B, C):
    pass

# Creating an object of class D
d = D()

# Calling the action method
d.action()  # Output: Action from B (B comes before C in MRO)

# Let's print the MRO for class D
print(D.mro())
# Output:
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# Since B comes before C in the MRO, the method from B is called first, 
# even though both B and C have an action method.
