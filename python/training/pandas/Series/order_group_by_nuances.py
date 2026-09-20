import pandas as pd

# Let's create a simple Series to play with
s = pd.Series([1, 3, 20, 2, 10, 1,3,4,5])

# GROUPBY WITH SORTING: Pandas is like a neat freak here, always sorting things out!
# By default, groupby sorts the groups because it assumes you want your results 
# in a nice, predictable order. Imagine having a tidy desk where everything is in
# alphabetical order. It's easy to find stuff, right? But sometimes, life (and data)
# isn't so neat and tidy...
for k, v in s.groupby(s // 10, sort=True):
    # Here, s // 10 creates groups based on the integer division of each value by 10.
    # Values less than 10 are grouped into '0' and those 10 or above into '1' and so on.
    print(k, v.tolist())
    # Output is sorted by the group key (0 first, then 1, etc.)

# GROUPBY WITHOUT SORTING: Now, let's see what happens when we tell Pandas to chill out a bit.
# When sort=False, Pandas respects the order of the data as it appears in the Series. 
# This is like your desk on a busy day - everything is where you left it, and you're 
# okay with the chaos... sometimes speed and originality beat order!
for k, v in s.groupby(s // 10, sort=False):
    print(k, v.tolist())
    # Now, groups appear in the order of their first appearance in the Series.
    # This might be faster for very large datasets, or when you care about the 
    # original order of your data.

# Let’s go back to Pandas' default nature of sorting groups.
# This time, we are not specifying 'sort', so Pandas does its usual thing.
for k, v in s.groupby(s // 10):
    print(k, v.tolist())
    # Again, sorted by group key (0, then 1) because that's the default behavior.

# LET'S HAVE SOME FUN WITH FUNCTIONS:
# Custom transformation function: Adding some humor, let's imagine we want to 
# "double the fun" by multiplying each value by 2, because why not?
def double_the_fun(x):
    return x * 2

# Custom aggregation function: Let's create a 'mean but rounded to the nearest 
# superhero level' function - it rounds the mean to the nearest 5.
def superhero_mean(x):
    return round(x.mean() / 5) * 5

# Custom aggregation function: Get the difference between max and min (like a 
# rollercoaster ride of data!)
def rollercoaster_range(x):
    return x.max() - x.min()

# Applying custom transformation function with groupby
transformed = s.groupby(s // 10).transform(double_the_fun)
print("Transformed Series (Double the Fun):")
print(transformed)

# Applying custom aggregation functions with groupby
aggregated_mean = s.groupby(s // 10).apply(superhero_mean)
aggregated_range = s.groupby(s // 10).apply(rollercoaster_range)
print("\nAggregated Mean Rounded to Nearest Superhero Level:")
print(aggregated_mean)
print("\nAggregated Rollercoaster Range:")
print(aggregated_range)

# Bonus: Grouping by even or odd, just for fun!
def even_odd(x):
    return "Even" if x % 2 == 0 else "Odd"

print(s)
for k, v in s.groupby(even_odd):
    print(f"\nGroup: {k}")
    print(v.tolist())
    # Grouping by 'Even' or 'Odd' values just to showcase Pandas' flexibility!

# If you want to group by the values of the Series being even or odd (not their index positions),
#  you need to apply the even_odd function directly to the values, not to the index. You can modify the groupby call like this
print(s.apply(even_odd))

for k, v in s.groupby(s.apply(even_odd)):
    print(f"\nGroup: {k}")
    print(v.tolist())
