# 🚨 Don't change the code below 👇
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Convert the two-digit input into separate numbers.
column = int(position[0])
row = int(position[1])

# Convert the user input into zero-based indexing to update the map list.
# Remember that the input's first number is for column and the second is for row.
# Subtracting 1 from each because lists are zero-indexed.
map[row - 1][column - 1] = "X"

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
print(f"{map}")
