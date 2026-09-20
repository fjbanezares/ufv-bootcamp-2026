# Understanding Lists in Python

# 1. Accessing Elements in a List
r = [1, -16, 15]

# Negative indices start counting from the end of the list.
print(r[-1])  # Outputs: 15 (last item)
print(r[-2])  # Outputs: -16 (second to last item)

# Here's how to access the last element using the length of the list.
print(r[len(r) - 1])  # Outputs: 15

# Accessing the first element.
print(r[0])  # Outputs: 1

# In Python, -0 is the same as 0.
print(r[-0])  # Outputs: 1 (first item)

# 2. List Slicing
s = [3, 186, 4431, 74400, 1048443]

# Slicing returns a portion of the list.
print(s[1:3])  # Outputs: [186, 4431]
print(s[1:-1])  # Outputs: [186, 4431, 74400]

# You can omit the start or the end index.
print(s[2:])  # Outputs: [4431, 74400, 1048443]
print(s[:2])  # Outputs: [3, 186]

# If you omit both indices, you get a copy of the original list.
print(s[:])  # Outputs: [3, 186, 4431, 74400, 1048443]

# 3. Comparing Lists and List Identities
t = s  # Here, t and s point to the exact same list in memory.

# "is" checks if two variables point to the same object.
print(t is s)  # Outputs: True

# We can create a new list that's a copy of an existing list.
r = s[:]  # This is a shallow copy.
print(r is s)  # Outputs: False (because they are two different objects)
print(r == s)  # Outputs: True (because their contents are identical)

# Other ways to copy a list:
u = s.copy()  # Using the copy method. Outputs: False for "u is s"
v = list(s)   # Using the list constructor.

# 4. Multiplying Lists
c = [21, 37]

# When you multiply a list, its content gets repeated.
d = c * 4
print(d)  # Outputs: [21, 37, 21, 37, 21, 37, 21, 37]

# This is a quick way to create a list with repeated values.
print([0] * 9)  # Outputs: [0, 0, 0, 0, 0, 0, 0, 0, 0]

# 5. Issues with Multiplying Lists Containing Mutable Inner Lists
s = [[-1, +1]] * 5
print(s)  # Outputs: [[-1, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 1]]

# Append 7 to the third list.
s[2].append(7)

# Now, let's see the effect this has:
# Outputs: [[-1, 1, 7], [-1, 1, 7], [-1, 1, 7], [-1, 1, 7], [-1, 1, 7]]
print(s)
# All sublists were modified! This is because they all point to the same object.

# 6. Working with List Methods
w = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

# You can find the index of a value in a list.
print(w.index('fox'))  # Outputs: 3

# If the value isn't in the list, it raises an error.
# Uncommenting the next line would raise a ValueError.
# print(w.index('unicorn'))

# Count how many times a value appears in a list.
print(w.count("the"))  # Outputs: 2

# You can check for the presence or absence of a value in a list.
print(37 in [1, 78, 9, 37, 34, 53])       # Outputs: True
print(78 not in [1, 78, 9, 37, 34, 53])  # Outputs: False

# 7. Deleting and Removing Elements from a List
u = ['jackdaws', 'love', 'my', 'big', 'sphinx', 'of', 'quartz']

# You can delete an item by its index.
del u[3]
print(u)  # Outputs: ['jackdaws', 'love', 'my', 'sphinx', 'of', 'quartz']

# Or remove the first occurrence of a value.
u.remove('jackdaws')
print(u)  # Outputs: ['love', 'my', 'sphinx', 'of', 'quartz']

# If the value isn't in the list, it raises an error.
# Uncommenting the next line would raise a ValueError.
# u.remove('pyramid')

# 8. Inserting into a List
a = ['I', 'accidentally', 'the', 'whole', 'universe']

# Insert a value at a particular index.
a.insert(2, "destroyed")
print(' '.join(a))  # Outputs: 'I accidentally destroyed the whole universe'

# 9. Concatenating and Extending Lists
m = [2, 1, 3]
n = [4, 7, 11]

# Combine two lists together.
k = m + n
print(k)  # Outputs: [2, 1, 3, 4, 7, 11]

# Add several values to the end of a list.
k += [18, 29, 47]
print(k)  # Outputs: [2, 1, 3, 4, 7, 11, 18, 29, 47]

# Another way to add values from another list or iterable.
k.extend([76, 129, 199])
print(k)  # Outputs: [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 129, 199]

# 10. Reversing and Sorting Lists
g = [1, 11, 21]

# You can reverse the order of a list's items.
g.reverse()
print(g)  # Outputs: [21, 11, 1]

d = [17, 41, 29]

# Sort the items of a list in ascending order.
d.sort()
print(d)  # Outputs: [17, 29, 41]

# Or in descending order.
d.sort(reverse=True)
print(d)  # Outputs: [41, 29, 17]

# You can also sort by a custom function, such as string length.
h = ['not', 'perplexing', 'do', 'handwriting', 'family',
     'where', 'I', 'illegibly', 'know', 'doctors']
h.sort(key=len)
# Outputs: 'I do not know where doctors handwriting family perplexing illegibly'
print(' '.join(h))

# Python also offers a way to get a sorted copy of a list.
x = [4, 9, 2, 1]
y = sorted(x)  # Original list remains unchanged.
print(x)  # Outputs: [4, 9, 2, 1]
print(y)  # Outputs: [1, 2, 4, 9]

# Likewise, you can get a reversed copy of a list.
p = [9, 3, 1, 0]
q = reversed(p)  # This gives you an iterator.
print(list(q))  # Outputs: [0, 1, 3, 9]
