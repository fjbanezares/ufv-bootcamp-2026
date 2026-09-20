# Understanding Python Sets

# Initial Set Creation
p = {33550336, 8128, 6, 496, 28}
print(p)  # Output: {33550336, 8128, 6, 496, 28}

# A set is a unique collection of items, unordered and unindexed.
print(type(p))  # Output: <class 'set'>

# Defining an empty dictionary.
d = {}
print(type(d))  # Output: <class 'dict'>

# The correct way to create an empty set in Python.
e = set()
print(e)  # Output: set()

# Constructing a set from a list.
s = set([2, 4, 16, 64, 4096, 65536, 262144])
print(s)  # Notice that order is not maintained.

# Converting a list with repeated items into a set to get unique values.
t = [1, 4, 2, 1, 7, 9, 9]
print(set(t))  # Output: {1, 2, 4, 7, 9}

# Membership testing: Check if a value is in the set or not.
q = {2, 9, 6, 4}
print(3 in q)  # Output: False
print(3 not in q)  # Output: True

# Adding elements to a set using `add`.
k = {81, 108}
k.add(54)  # Add single element
k.add(12)
k.add(108)  # Adding a repeated element won't change the set.
print(k)

# Using `update` to add multiple elements (from lists, sets, etc.).
k.update([37, 128, 97])
print(k)

# Removing elements from a set. `remove` will raise an error if the item is not present.
k.remove(97)
print(k)  # 97 is removed.
# k.remove(98)  # Uncommenting this will raise KeyError: 98

# The `discard` method removes the item if it exists, but does nothing if it doesn't.
k.discard(98)  # No error
print(k)

# Copying sets. Both `copy` and `set()` constructor can be used.
j = k.copy()
print(j)
m = set(j)
print(m)

# Set Operations: union, intersection, difference, symmetric_difference.
# These methods allow sets to be compared and combined in various ways.

# Sample data of people with different genetic traits.
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
smell_hcn = {'Harry', 'Amelia'}
taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}
o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
b_blood = {'Amelia', 'Jack'}
a_blood = {'Harry'}
ab_blood = {'Joshua', 'Lola'}

# Union: combines two sets.
# Note: The order of the union operations doesn't matter.
print(blond_hair.union(smell_hcn))
print(blond_hair.union(smell_hcn) == smell_hcn.union(blond_hair))  # Output: True

# Intersection: finds common elements in two sets.
# Note: The order of the intersection operations doesn't matter.
print(blond_hair.intersection(taste_ptc))
print(blond_hair.intersection(taste_ptc) ==
      taste_ptc.intersection(blond_hair))  # Output: True

# Difference: elements in the first set that aren't in the second.
# Note: The order matters for difference.
print(blond_hair.difference(smell_hcn))
print(blond_hair.difference(smell_hcn) ==
      smell_hcn.difference(blond_hair))  # Output: False

# Symmetric Difference: elements that are in one of the sets, but not in both.
print(blond_hair.symmetric_difference(taste_ptc))
print(blond_hair.symmetric_difference(taste_ptc) ==
      taste_ptc.symmetric_difference(blond_hair))  # Output: True

# Subset and Superset.
print(smell_hcn.issubset(blond_hair))  # Output: True
print(taste_ptc.issuperset(smell_hcn))  # Output: True

# Disjoint sets have no elements in common.
print(a_blood.isdisjoint(o_blood))  # Output: True
