# multiply_list_references.py

# Dear friend, in this script, we'll explore the behavior of the multiplication operator (*) with lists in Python.
# We'll pay special attention to how Python handles references to mutable objects.
# Please read through the comments to understand each step thoroughly. Thank you!

# PLEASE NOTE: When you multiply a list containing mutable objects, 
# Python creates multiple references to the SAME object, not distinct copies.

# Let's start by creating a simple list containing a mutable sublist.
sublist = [-1, +1]  # This is a simple sublist

# Now, let's multiply this list by 5 to create a new list 's'.
s = [sublist] * 5

# Let's print the list 's' to see what we have created.
print("Our list 's' after multiplication:")
print(s)
# Output will be:
# [[-1, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 1]]
# At first glance, it looks like we have five separate sublists. 
# However, please be careful, my friend! These are not distinct objects.

# Let's modify one of the sublists in 's'.
s[2].append(7)  # Adding '7' to the third sublist in 's'.

# Now, let's print 's' again to see what happened.
print("\nOur list 's' after appending 7 to the third sublist:")
print(s)
# Output will be:
# [[-1, 1, 7], [-1, 1, 7], [-1, 1, 7], [-1, 1, 7], [-1, 1, 7]]
# Oh no! All sublists were modified! Why did this happen? 

# Explanation:
# -------------
# Each sublist in 's' is a reference (pointer) to the same sublist object, 'sublist'.
# When we modified one sublist, we actually modified the single underlying object.
# So, all "copies" of the sublist reflect this change. 

# This behavior is crucial to understand when working with lists of mutable objects in Python.
# If you want distinct sublists (independent objects), you must create independent copies.

# PLEASE BE CAREFUL when multiplying lists containing mutable objects!

# Let's create a similar list, but this time, we'll use a list comprehension to ensure independent sublists.
s_distinct = [[-1, +1] for _ in range(5)]

# Now, let's print 's_distinct' to see our new creation.
print("\nOur distinct list 's_distinct' created with a list comprehension:")
print(s_distinct)
# Output will be:
# [[-1, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 1]]
# It looks similar to 's', but this time, each sublist is a separate object.

# Let's modify the third sublist in 's_distinct' to see what happens.
s_distinct[2].append(7)

# Now, let's print 's_distinct' again.
print("\nOur list 's_distinct' after appending 7 to the third sublist:")
print(s_distinct)
# Output will be:
# [[-1, 1], [-1, 1], [-1, 1, 7], [-1, 1], [-1, 1]]
# Hooray! Only the third sublist was modified. This is the behavior we want for independent sublists.

# THANK YOU for taking the time to explore this concept deeply with me!
# PLEASE always be mindful of how Python handles object references, especially with mutable objects.

# Let's wrap up with a recap:
# ---------------------------
# Multiplying a list containing mutable objects creates references to the same object.
# This can lead to unintended modifications across "copies" since they all point to the same object.
# Using a list comprehension ensures each sublist is a distinct object, preventing such issues.
