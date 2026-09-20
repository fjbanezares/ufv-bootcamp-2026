# Python Dictionaries

# A dictionary with keys and values, where keys are terms related to programming and values are their definitions.
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# To retrieve a specific value from a dictionary, you index it with the corresponding key.
# This would print the definition of "Function".
# print(programming_dictionary["Function"])

# You can add a new key-value pair to a dictionary directly.
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Create an empty dictionary. It has no keys or values.
empty_dictionary = {}

# To wipe or clear a dictionary, you can reassign it to an empty dictionary.
# programming_dictionary = {}
# print(programming_dictionary)

# You can update the value of an existing key in a dictionary.
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

# Looping through a dictionary gives access to each key.
# You can then access the corresponding value using the key.
# for key in programming_dictionary:
#    print(key)
#    print(programming_dictionary[key])

#######################################

# A simple dictionary with countries as keys and their capitals as values.
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# You can nest a list inside a dictionary as a value.
# Here, each country key has a list of cities visited as its value.
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Dictionaries can also be nested within other dictionaries.
# Here, each country has another dictionary as its value, which contains cities visited and total visits.
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# You can also nest dictionaries inside a list.
# This makes each item of the list a dictionary with its own set of key-value pairs.
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]
