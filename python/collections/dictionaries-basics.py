# Dictionary Initialization

# Initializing a dictionary using curly braces
from pprint import pprint as pp
urls = {
    'Pluralsight': 'http://pluralsight.com',
    'Sixty North': 'http://sixty-north.com',
    'Microsoft': 'http://microsoft.com'
}
# Accessing values: When you provide a key, the dictionary returns its associated value.
print(urls['Pluralsight'])  # Expected Output: 'http://pluralsight.com'

# Using the dict() constructor
# Converting a list of tuples into a dictionary.
names_and_ages = [('Alice', 32), ('Bob', 48), ('Charlie', 28), ('Daniel', 33)]
d = dict(names_and_ages)
# Expected Output: {'Alice': 32, 'Bob': 48, 'Charlie': 28, 'Daniel': 33}
print(d)

# Another way of initializing dictionary using dict() with explicit key=value arguments.
phonetic = dict(a='alfa', b='bravo', c='charlie',
                d='delta', e='echo', f='foxtrot')
print(phonetic)  # Expected Output: {'a': 'alfa', 'b': 'bravo', ...}

# Copying dictionaries
e = d.copy()  # Creates a shallow copy of the dictionary.
f = dict(e)   # Another way to create a shallow copy.

# The `update` method merges two dictionaries.
g = dict(wheat=0xF5DEB3, khaki=0xF0E68C, crimson=0xDC143C)
f.update(g)
# Expected Output: Merged dictionary with values from both 'e' and 'g'.
print(f)

# You can update existing key-value pairs and add new ones using `update`.
stocks = {'GOOG': 891, 'AAPL': 416, 'IBM': 194}
stocks.update({'GOOG': 894, 'YHOO': 25})
# Expected Output: {'GOOG': 894, 'AAPL': 416, 'IBM': 194, 'YHOO': 25}
print(stocks)

# Iterating through dictionaries
colors = dict(
    aquamarine='#7FFFD4', burlywood='#DEB887', chartreuse='#7FFF00', cornflower='#6495ED',
    firebrick='#B22222', honeydew='#F0FFF0', maroon='#B03060', sienna='#A0522D'
)
# Iterating through keys
for key in colors:
    # Prints each key with its corresponding value.
    print(f"{key} => {colors[key]}")

# Iterating through values directly
for value in colors.values():
    print(value)

# Iterating using both keys and values
for key, value in colors.items():
    print(f"{key} => {value}")  # Prints key-value pairs.

# Key existence can be checked using 'in'.
symbols = dict(
    usd='$', gbp='£', nzd='$', krw='₩', eur='€', jpy='¥',  nok='kr', hhg='Pu', ils='₪'
)
# Expected Output: True (because 'nzd' is a key in 'symbols')
print('nzd' in symbols)
# Expected Output: True (because 'mkd' is not a key in 'symbols')
print('mkd' not in symbols)

# Deleting key-value pairs using 'del'
z = {'H': 1, 'Tc': 43, 'Xe': 54, 'Fy': 137, 'Rf': 104, 'Fm': 100}
del z['Fy']  # Removes the key 'Fy' and its value.
print(z)  # 'Fy' key and its value should be absent in the output.

# Modifying values in the dictionary.
m = {
    'H': [1, 2, 3],
    'He': [3, 4],
    'Li': [6, 7],
    'Be': [7, 9, 10],
    'B': [10, 11],
    'C': [11, 12, 13, 14]
}
# Appending multiple values to the list associated with the 'H' key.
m['H'] += [4, 5, 6, 7]
print(m['H'])  # Expected Output: [1, 2, 3, 4, 5, 6, 7]

# If a key doesn't exist, this syntax will add the key with the provided value.
m['N'] = [13, 14, 15]
print(m['N'])  # Expected Output: [13, 14, 15]

# Using pprint (pretty-print) for better visualization of the dictionary structure.
pp(m)
