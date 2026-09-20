# Introduction to Dictionaries
# A dictionary is a mutable, unordered collection of items. 
# Each item is a pair of a unique key and its corresponding value.
# Dictionaries are optimized for retrieving values when we know the key.

# PLEASE pay attention to how we create dictionaries, THANK YOU! :)

# 1. Creating a dictionary using curly braces
person = {"name": "John", "age": 30, "city": "NY"}
print(person)  # Output: {'name': 'John', 'age': 30, 'city': 'NY'}

# 2. Creating a dictionary using the dict() constructor with keyword arguments
person = dict(name="John", age=30, city="NY")
print(person)  # Output: {'name': 'John', 'age': 30, 'city': 'NY'}

# 3. Creating a dictionary using the dict() function with a list of (key, value) tuples
person = dict([("name", "John"), ("age", 30), ("city", "New York")])
print(person)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# 4. Creating a dictionary using the zip() function
keys = ["name", "age", "city"]
values = ["John", 30, "New York"]
person = dict(zip(keys, values))
print(person)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# 5. Dictionary comprehension - Creating a dictionary from an iterable
squared = {x: x**2 for x in range(5)}
print(squared)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# PLEASE remember that dictionaries are incredibly versatile, THANK YOU!

# Accessing and Modifying Dictionary Values

# Accessing values using keys
print(person["name"])  # Output: John

# Modifying values
person["age"] = 31
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

# Adding a new key-value pair
person["email"] = "john@example.com"
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'email': 'john@example.com'}

# Removing a key-value pair using del
del person["city"]
print(person)  # Output: {'name': 'John', 'age': 31, 'email': 'john@example.com'}

# Dictionary Methods

# 1. get(): Returns the value for a given key if it exists, else returns a default value.
value = person.get("name", "not found")
print(value)  # Output: John

value = person.get("city", "not found")
print(value)  # Output: not found

# 2. items(): Returns pairs of keys and values.
print(person.items())  # Output: dict_items([('name', 'John'), ('age', 31), ('email', 'john@example.com')])

# 3. keys(): Returns the keys of the dictionary.
print(person.keys())  # Output: dict_keys(['name', 'age', 'email'])

# 4. values(): Returns the values of the dictionary.
print(person.values())  # Output: dict_values(['John', 31, 'john@example.com'])

# 5. pop(): Removes a key-value pair based on the key and returns the value.
email = person.pop("email")
print(email)  # Output: john@example.com
print(person)  # Output: {'name': 'John', 'age': 31}

# 6. popitem(): Removes and returns the last key-value pair from the dictionary.
person["city"] = "New York"
last_item = person.popitem()
print(last_item)  # Output: ('city', 'New York')
print(person)  # Output: {'name': 'John', 'age': 31}

# 7. clear(): Removes all key-value pairs from the dictionary.
person.clear()
print(person)  # Output: {}

# 8. copy(): Returns a shallow copy of the dictionary.
person = {"name": "John", "age": 30}
person_copy = person.copy()
print(person_copy)  # Output: {'name': 'John', 'age': 30}

# 9. update(): Merges two dictionaries. If keys overlap, values from the second dictionary are used.
dict1 = {"apple": "fruit", "broccoli": "vegetable"}
dict2 = {"banana": "fruit", "broccoli": "green vegetable"}
dict1.update(dict2)
print(dict1)  # Output: {'apple': 'fruit', 'broccoli': 'green vegetable', 'banana': 'fruit'}

# 10. setdefault(): Returns the value for a key if it exists. If not, inserts key with a value (default is None).
fruit = dict1.setdefault("grape", "fruit")
print(fruit)  # Output: fruit
print(dict1)  # Output: {'apple': 'fruit', 'broccoli': 'green vegetable', 'banana': 'fruit', 'grape': 'fruit'}

# Interesting Topics in Dictionaries

# 1. Dictionary fromkeys() method - Creates a dictionary from a sequence of keys and a single value.
keys = ["a", "b", "c"]
default_value = 0
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}

# 2. Handling dictionaries in a multithreaded environment
# Dictionaries are mutable and not thread-safe. Be cautious when accessing/modifying dictionaries in multithreaded applications.

import threading  # Importing the threading module to create and manage threads in Python.

# Define a function that will be executed by each thread.
def update_dict(shared_dict, key, value):
    # This function takes three arguments:
    # - shared_dict: A shared dictionary that all threads will modify.
    # - key: The key to add or update in the dictionary.
    # - value: The value associated with the key in the dictionary.
    
    shared_dict[key] = value  # Update the dictionary with the new key-value pair.
    # Since dictionaries are mutable objects in Python, this change will affect the original dictionary
    # shared by all threads.

# Initialize an empty dictionary that will be shared among threads.
shared_dict = {}  # This dictionary is empty initially and will be updated by multiple threads.

# Initialize an empty list to keep track of all the thread objects.
threads = []  # This list will hold all the thread objects created in the loop below.

# Create and start multiple threads.
for i in range(50):  # Loop five times to create five threads.
    # Create a new Thread object.
    # target specifies the function that the thread should execute, which is `update_dict`.
    # args is a tuple that contains the arguments to pass to the target function.
    # In this case, we're passing the shared_dict, a unique key (f"key{i}"), and a unique value (f"value{i}").
    thread = threading.Thread(target=update_dict, args=(shared_dict, f"key{i}", f"value{i}"))
    
    # Append the created thread to the list of threads.
    threads.append(thread)  # This keeps track of the thread so we can manage it later.

    # Start the thread's activity.
    # When this method is called, the thread begins executing the target function (`update_dict`).
    thread.start()  # The thread will start running `update_dict`, modifying the shared dictionary.

# Wait for all threads to complete their execution.
for thread in threads:  # Loop over the list of threads.
    # Call the join() method on each thread object.
    # This method blocks the calling thread (main thread) until the thread whose join() method is called is terminated.
    # In other words, it waits for the thread to finish its execution.
    thread.join()  # Ensures all threads have completed before the program continues.

# By the time the loop completes, all threads have finished updating the shared dictionary.
# This synchronization ensures that the final state of `shared_dict` includes all updates from all threads.


print(shared_dict)  # Output may vary due to the race condition

# THANK YOU for sticking with us through this journey of dictionaries!
# PLEASE remember to practice and explore more to solidify your understanding.
# Dictionaries are powerful tools in Python, and mastering them will make your code more efficient and effective!

# That's all for now! Keep coding and have fun! :)
