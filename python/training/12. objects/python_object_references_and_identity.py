# Let's start by demonstrating that everything in Python is an object.
# Please observe that even numbers, strings, and functions are objects.

# Example 1: Integer object
x = 42  # x is an integer object
print(type(x))  # <class 'int'>
print(id(x))  # Outputs the memory address of x, unique to this integer object

# Example 2: String object
y = "hello"  # y is a string object
print(type(y))  # <class 'str'>
print(id(y))  # Outputs the memory address of y, unique to this string object

# Example 3: Function object
def foo():
    pass  # foo is a function object

print(type(foo))  # <class 'function'>
print(id(foo))  # Outputs the memory address of foo, unique to this function object

# Thank you for following along! Now, let's explore identity and assignment.

# When you assign one variable to another, they both point to the same object.
# They don't create a copy; instead, they reference the same memory location.

x = 500  # x is an integer object
y = x  # y is now referencing the same integer object as x
print(y is x)  # True, because y and x point to the same object
print(id(x), id(y))  # Both will print the same memory address

# Let's modify a mutable object to see how references work in functions.

def modify(lst):
    """This function modifies the list by appending an element to it."""
    lst.append(4)  # Modifies the list that lst points to

# Please note that lists in Python are mutable objects.

x = [1, 2, 3]  # x is a list object, which is mutable
modify(x)  # We pass the list to the modify function
print(x)  # Outputs: [1, 2, 3, 4]

# As you can see, the original list was modified. This demonstrates that when we pass
# a mutable object to a function, we're passing a reference to that object, not a copy.

# Let's explore more examples to further clarify object references and identity.

# Example 4: Assigning a new value to y does not affect x because integers are immutable.

y = 1000  # Now y references a new integer object
print(y is x)  # False, because y now points to a different object than x

# Example 5: Copying a list creates a new list object, but not a new reference.

x = [10, 20, 30]
y = x[:]  # y is a shallow copy of x, but a new list object
print(y is x)  # False, because y is a different object
print(y == x)  # True, because the contents of y are equal to those of x

# Thank you for your attention! Let's continue with more examples involving different object types.

# Example 6: Modifying a mutable object through one reference affects all references.

a = [5, 6, 7]
b = a  # b is another reference to the same list
b.append(8)  # Modify the list through reference b
print(a)  # Outputs: [5, 6, 7, 8]
print(b)  # Outputs: [5, 6, 7, 8]

# Both a and b reflect the change because they reference the same object.

# Example 7: Tuples are immutable, so assigning one to another variable does not link them.

t1 = (1, 2, 3)  # t1 is a tuple object, which is immutable
t2 = t1  # t2 is referencing the same tuple as t1
t3 = (1, 2, 3)  # t3 is a new tuple with the same values
print(t1 is t2)  # True, t1 and t2 point to the same object
print("fuck...", t1 is t3)  # False, t1 and t3 are different objects even though they have the same content 
# Python has an optimization mechanism that caches small immutable objects like strings and numbers.
#  This can extend to tuples that contain immutable objects. If t1 and t3 are small and have the same content, 
# Python might optimize memory usage by pointing t3 to the same object as t1 instead of creating a new one.
print(id(t1), id(t2), id(t3))  # Both will print the same memory address
t4 = (1, 2, 3)  # t3 is a new tuple with the same values
print(id(t1), id(t2), id(t3), id(t4))  # Both will print the same memory address

t1 = (1, 2, 3, [])  # Adding a mutable object (list) inside the tuple
t3 = (1, 2, 3, [])  # Another tuple with the same values

print(t1 is t3)  # This will likely return False because of the mutable element
print(id(t1), id(t2), id(t3))  # Both will print the same memory address


# IF YOU GO DEEP YOU GO HARD


# Example 8: Dictionary example to demonstrate object references.

d1 = {"key": "value"}
d2 = d1  # d2 references the same dictionary as d1
d2["key"] = "new value"  # Modify the dictionary through d2
print(d1)  # Outputs: {'key': 'new value'}
print(d2)  # Outputs: {'key': 'new value'}

# Both d1 and d2 reflect the change because they reference the same dictionary object.

# I hope these examples help you understand how Python handles objects, references, and identity.
# Please feel free to experiment with these concepts on your own. Thank you again!

