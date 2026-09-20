# 🚀 Let's explore the world of conditional statements and boolean logic!

# Basic conditional statement example with some fun:
age = 20
if age >= 18:
    print("🎉 You're an adult!")
else:
    print("🧒 You're still a minor!")

# Using elif to check multiple conditions:
height = 150
if height > 180:
    print("🏀 You should play basketball!")
elif height > 160:
    print("⚽ Maybe try soccer!")
else:
    print("🤸 Gymnastics could be your thing!")

# Demonstrating comparison operators:
a, b = 5, 10
print(f"Is {a} equal to {b}? {a == b}")
print(f"Is {a} not equal to {b}? {a != b}")
print(f"Is {a} less than {b}? {a < b}")
print(f"Is {a} greater than or equal to {b}? {a >= b}")

# Logical operators with fun examples:
likes_python = True
has_free_time = False

if likes_python and has_free_time:
    print("🎓 Time to learn more Python!")
elif likes_python and not has_free_time:
    print("⏰ You need to find some free time to code!")
else:
    print("🤔 Maybe give Python a try sometime!")

# Short-circuit evaluation:
# Using 'and' - if the first condition is False, it won't check the second condition.
print("Checking False and print('This won\'t print.'):")
print(False and print("This won't print."))  # This won't print anything

# Using 'or' - if the first condition is True, it won't check the second condition.
print("Checking True or print('This won\'t print.'):")
print(True or print("This won't print."))  # This won't print anything

# Example with 'is' and 'is not':
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(f"x0 is y0: /{x[0] is y[0]}")  # True, because we are reusing integers
print(f"x equal y: {x == y}")  # True
print(f"x is z: {x is z}")  # True, because z points to the same object as x
print(f"x is y: {x is y}")  # False, because x and y are different objects in memory
print(f"x is not y: {x is not y}")  # True, because x and y are not the same object


# Fun example of falsy and truthy values:
happy = False
if happy:
    print("😃 I'm happy!")
else:
    print("😔 I'm not happy...")


alto = 5
ancho = 17
espacio_maximo = 22

if alto + ancho < espacio_maximo:
    print("cabe")
else:
    print("no cabe") 

print("el ancho es" , alto + ancho, " y esta genial")   
# Checking if a list is empty:
my_list = []
if my_list:
    print("📚 The list has items.")
else:
    print("📭 The list is empty.")

# Demonstrating truthiness of non-boolean values:
name = "Alice"
if name:
    print(f"👋 Hello, {name}!")
else:
    print("🔍 No name provided.")

print("This is a raw string.  \n  newline.")
print(r"This is a raw string.  \n not newline.")
print("This is a raw string.  \\n not newline.")
print(f"x is not y: \\{{x}}") 



# Custom object truthiness example:
class Person:
    def __init__(pepito, arg1, arg2):
        pepito.name = arg1
        pepito.age = arg2

    def __bool__(juanito):
        # Consider a person 'truthy' if they are an adult (18 or older)
        return juanito.age >= 18

# Creating instances of Person
teenager = Person("Alice", 16)
adult = Person("Bob", 30)

if teenager:
    print(f"{teenager.name} is considered truthy.")
else:
    print(f"{teenager.name} is considered falsy.")

if adult:
    print(f"{adult.name} is considered truthy.")
else:
    print(f"{adult.name} is considered falsy.")
