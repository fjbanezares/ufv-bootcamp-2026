# Mixin 1
class WalkMixin:
    def walk(self):
        print(f"{self.__class__.__name__} is walking.")

# Mixin 2


class TalkMixin:
    def talk(self):
        print(f"{self.__class__.__name__} is talking Talk Mixin.")

# Mixin 3


class EatMixin:
    def eat(self):
        print(f"{self.__class__.__name__} is eating.")

    def talk(self):
        print(f"{self.__class__.__name__} is talking Eat Mixin.")

# Combining multiple mixins


class Person(WalkMixin, TalkMixin, EatMixin):
    def __init__(self, name):
        self.name = name


class Person2(EatMixin, WalkMixin, TalkMixin):
    def __init__(self, name):
        self.name = name


# Creating an object and calling methods from mixins
p = Person("Alice")
p.walk()
p.talk()
p.eat()

p = Person2("Bob")
p.walk()
p.talk()
p.eat()


class A:
    def show(self):
        print("Method in class A")


class B(A):
    def show(self):
        print("Method in class B")


class C(A):
    def show(self):
        print("Method in class C")


class D(B, C):
    pass


# Create an instance of class D
obj = D()

# Call the show() method
obj.show()

print(D.__mro__)
# Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

print(D.mro())
# Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
