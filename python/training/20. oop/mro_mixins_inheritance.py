# Let's start with some mixins. Mixins add specific behavior to a class.

# Mixin 1: WalkMixin
class WalkMixin:
    def walk(self):
        print(f"{self.name} is walking!")  # Thanks for walking!

# Mixin 2: TalkMixin
class TalkMixin:
    def talk(self):
        print(f"{self.name} is talking!")  # Thanks for talking!

# Mixin 3: FlyMixin
class FlyMixin:
    def fly(self):
        print(f"{self.name} is flying!")  # Thanks for flying!

# Mixin 4: SwimMixin
class SwimMixin:
    def swim(self):
        print(f"{self.name} is swimming!")  # Thanks for swimming!

# Mixin 5: SuperJumpMixin
class SuperJumpMixin:
    def jump(self):
        print(f"{self.name} is making a super jump!")  # Thanks for jumping!

# Now let's create a base Person class.
# This class will take a name and use mixins.

class Person(WalkMixin, TalkMixin):
    def __init__(self, name):
        self.name = name  # We store the name of the person
        print(f"Hello, {self.name}, you can walk and talk!")

# Let's create a new class SuperHero which adds more mixins
# This class inherits from Person and adds more abilities.

class SuperHero(Person, FlyMixin, SwimMixin, SuperJumpMixin):
    def __init__(self, name):
        super().__init__(name)  # Thanks to super, we initialize the name
        print(f"{self.name} can now fly, swim, and super jump too!")  # Thanks for having extra powers!

# Let's now define a special Villain class with some unique behavior.
# Villain will also inherit from some mixins, but the order will change.

class Villain(SwimMixin, FlyMixin, TalkMixin):
    def __init__(self, name):
        self.name = name
        print(f"{self.name} can swim, fly, and talk, but in a villainous way!")  # Watch out!

# Now let's add even more complexity with an AntiHero
# An AntiHero shares traits from both SuperHero and Villain.

class AntiHero(SuperHero, Villain):
    def __init__(self, name):
        super().__init__(name)  # We initialize using the MRO order
        print(f"{self.name} is a complex character!")  # Thanks for being complicated!

# Now, let's create a few objects and see the MRO in action.

# Create a simple person who can walk and talk
p = Person("Bruce Wayne")
p.walk()  # Output: Bruce Wayne is walking!
p.talk()  # Output: Bruce Wayne is talking!

# Create a SuperHero with all the mixins
hero = SuperHero("Superman")
hero.walk()  # Superman can walk
hero.talk()  # Superman can talk
hero.fly()   # Superman can fly
hero.swim()  # Superman can swim
hero.jump()  # Superman can super jump!

# Now create a villain
villain = Villain("Lex Luthor")
villain.talk()  # Lex Luthor is talking
villain.fly()   # Lex Luthor can fly
villain.swim()  # Lex Luthor can swim

# Finally, let's create an AntiHero who mixes it all up.
antihero = AntiHero("Deadpool")
antihero.walk()  # Deadpool can walk
antihero.talk()  # Deadpool can talk (which mixin will be used?)
antihero.fly()   # Deadpool can fly
antihero.swim()  # Deadpool can swim
antihero.jump()  # Deadpool can super jump!

# Let's inspect the MRO for AntiHero to understand the method resolution order.
print(AntiHero.mro())  # What does the MRO look like? Let's see!

# Thanks for exploring the MRO! Python uses the C3 Linearization algorithm 
# to determine the MRO in multiple inheritance.
