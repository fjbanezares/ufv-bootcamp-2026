# Mixin 1: WalkMixin
class WalkMixin:
    def walk(self):
        # Now we are using the person's name instead of the class name.
        print(f"{self.name} is walking")  # Thanks for walking!

# Mixin 2: TalkMixin
class TalkMixin:
    def talk(self):
        # Now we are using the person's name instead of the class name.
        print(f"{self.name} is talking")  # Thanks for talking!

# Mixin 3: EatMixin
class EatMixin:
    def eat(self):
        # Now we are using the person's name instead of the class name.
        print(f"{self.name} is eating")  # Thanks for eating!

# Mixin 4: SleepMixin
class SleepMixin:
    def sleep(self):
        # Now we are using the person's name instead of the class name.
        print(f"{self.name} is sleeping")  # Thanks for sleeping!

# Combining multiple mixins into the Person class
class Person(WalkMixin, TalkMixin, EatMixin, SleepMixin):
    def __init__(self, name):
        self.name = name  # Now the person has a name!
    
    def introduce(self):
        print(f"Hello, I am {self.name}")  # Thanks for introducing yourself!

# Let's test it
p = Person("Alice")

# Calling methods from mixins (inherited behavior)
p.walk()    # Output: Alice is walking
p.talk()    # Output: Alice is talking
p.eat()     # Output: Alice is eating
p.sleep()   # Output: Alice is sleeping

# Now let's create the SuperPerson class
class SuperPerson(Person, WalkMixin):
    def fly(self):
        # Special method for SuperPerson to fly
        print(f"{self.name} is flying")  # Thanks for flying!

sp = SuperPerson("Super Alice")

# Calling the SuperPerson methods
sp.walk()    # Output: Super Alice is walking
sp.talk()    # Output: Super Alice is talking
sp.eat()     # Output: Super Alice is eating
sp.sleep()   # Output: Super Alice is sleeping
sp.fly()     # Output: Super Alice is flying
