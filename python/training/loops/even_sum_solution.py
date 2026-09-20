# We start the total at 0, as this will be used to keep a running sum of even numbers.
total = 0

# The range function can be used with three parameters: start, stop, and step.
# Start: The first number in the range (inclusive).
# Stop: The number to stop at, but not include.
# Step: The difference between each successive number in the range.
# Here, we start at 2 (the first even number), stop at 101 (as 100 needs to be included), and step by 2 (to get every even number).
for number in range(2, 101, 2):
    # We add the current even number to our running total.
    total += number

# Finally, we print out the sum of all even numbers between 1 and 100.
print(total)
