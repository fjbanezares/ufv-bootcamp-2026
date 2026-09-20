import pandas as pd

# Creating a sample Series with an index
new_row = pd.Series({'A': 7, 'B': 8, 'C': 9}, name='c')

# Displaying the original Series
print("Original Series:")
print(new_row)
print("\n")

# Transposing the Series by converting it to a DataFrame and then using .T
# Please note: .T is an attribute that transposes the DataFrame
new_row_transposed = new_row.to_frame().T

# Displaying the transposed Series
print("Transposed Series (now a single-row DataFrame):")
print(new_row_transposed)
print("\n")

# Visual representation of the transposition process
print("Visual Representation:")
print("Before Transposition:       After Transposition:")
print("Index | Values              Columns | Index")
print("----------------              -------------------")
print("  A   |    7                |     A  B  C  ")
print("  B   |    8                |  c  7  8  9  ")
print("  C   |    9")
print("\n")

# Inserting the transposed Series into a DataFrame
df = pd.DataFrame({
    'A': [1, 4],
    'B': [2, 5],
    'C': [3, 6]
}, index=['a', 'b'])

print("Original DataFrame:")
print(df)
print("\n")

# Concatenating the transposed Series as a new row
# Thank you for paying attention, please see how we insert the new row
df = pd.concat([df, new_row_transposed])

print("DataFrame after inserting the transposed Series as a new row:")
print(df)
print("\n")

# Another example using transposition for data alignment

# Creating a new Series that needs to be transposed for alignment
another_row = pd.Series({'A': 10, 'B': 11, 'C': 12}, name='d')

print("Another Series:")
print(another_row)
print("\n")

# Transposing the Series and inserting it
another_row_transposed = another_row.to_frame().T

# Please remember: this transposed Series can now be easily concatenated
df = pd.concat([df, another_row_transposed])

print("DataFrame after inserting another transposed Series:")
print(df)
print("\n")

# Final note: Using transposition is a powerful tool when working with data alignment in Pandas.
# Thank you for learning about the transposition of a Series in Pandas!
