import pandas as pd

# Step 1: Creating a Basic Series Without a Specified Index
# Please note: When creating a Series without a specified index, Pandas automatically assigns an integer index starting from 0.
basic_series = pd.Series([1, 2, 3, 4, 5])

print("Basic Series without an explicit index:")
print(basic_series)
print("\n")

# Output:
# Basic Series without an explicit index:
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

# Please observe that this Series uses default integer indexing, which might not be ideal for adding to a DataFrame as a row later.


# Step 2: Creating a Series with a Specified Index
# Please, always consider creating a Series with a custom index to make your data more descriptive and easier to manipulate.
indexed_series = pd.Series([1, 2, 3, 4, 5], index=['A', 'B', 'C', 'D', 'E'])

print("Series with a custom index:")
print(indexed_series)
print("\n")

# Output:
# Series with a custom index:
# A    1
# B    2
# C    3
# D    4
# E    5
# dtype: int64

# Thank you for understanding the importance of having a custom index!


# Step 3: Creating a Simple DataFrame
df = pd.DataFrame({
    'A': [10, 20],
    'B': [30, 40],
    'C': [50, 60]
})

print("Original DataFrame:")
print(df)
print("\n")

# Output:
# Original DataFrame:
#     A   B   C
# 0  10  30  50
# 1  20  40  60


# Step 4: Adding a Series without a Custom Index as a New Row
# Let's see what happens when we add a Series without a custom index to the DataFrame.
# Please notice how this can lead to misalignment.
df_with_basic_series = pd.concat([df, basic_series.to_frame().T])

print("DataFrame after adding the Series without a custom index:")
print(df_with_basic_series)
print("\n")

# Output:
# DataFrame after adding the Series without a custom index:
#       A     B     C    0    1    2    3    4
# 0  10.0  30.0  50.0  NaN  NaN  NaN  NaN  NaN
# 1  20.0  40.0  60.0  NaN  NaN  NaN  NaN  NaN
# 0   NaN   NaN   NaN  1.0  2.0  3.0  4.0  5.0

# Thank you for seeing how using a Series without a proper index leads to columns being created with numbers as headers,
# which causes misalignment with the DataFrame columns.

# Step 5: Adding a Properly Indexed Series to a DataFrame
# Let's add a properly indexed Series that matches the DataFrame columns.

proper_series = pd.Series({'A': 70, 'B': 80, 'C': 90}, name='NewRow')

print("Proper Series with matching DataFrame columns:")
print(proper_series)
print("\n")

# Output:
# Proper Series with matching DataFrame columns:
# A    70
# B    80
# C    90
# Name: NewRow, dtype: int64

# Adding this Series to the DataFrame as a new row. 
df_with_proper_series = pd.concat([df, proper_series.to_frame().T])

print("DataFrame after adding the properly indexed Series:")
print(df_with_proper_series)
print("\n")

# Output:
# DataFrame after adding the properly indexed Series:
#          A     B     C
# 0     10.0  30.0  50.0
# 1     20.0  40.0  60.0
# NewRow 70.0  80.0  90.0

# Please observe how the properly indexed Series aligns perfectly with the DataFrame columns.
# The name 'NewRow' is important because it labels the new row in the DataFrame. If we omitted the name, the new row would have a numeric index.


# Step 6: What Happens If We Omit the Series Name?
# Please see what happens if we omit the Series name. 

unnamed_series = pd.Series({'A': 100, 'B': 110, 'C': 120})  # Note: No 'name' parameter

# Adding the unnamed Series to the DataFrame
df_with_unnamed_series = pd.concat([df_with_proper_series, unnamed_series.to_frame().T])

print("DataFrame after adding an unnamed Series:")
print(df_with_unnamed_series)
print("\n")

# Output:
# DataFrame after adding an unnamed Series:
#            A      B      C
# 0       10.0   30.0   50.0
# 1       20.0   40.0   60.0
# NewRow  70.0   80.0   90.0
# 0      100.0  110.0  120.0

# Thank you for noticing the difference! Without a 'name', the Series is added with a default numeric index (0 in this case).
# It may not be descriptive and can lead to confusion if not handled properly.

# Step 7: Adding More Complex Data to a DataFrame Using Transpose
# Finally, let's add a more complex data row using transpose to fit into a DataFrame.

extended_df = pd.DataFrame({
    'A': [10, 20, 30],
    'B': [40, 50, 60],
    'C': [70, 80, 90],
    'D': [100, 110, 120]
})

print("Extended DataFrame:")
print(extended_df)
print("\n")

# Creating a Series to add as a new row, which needs transposition
new_series = pd.Series({'A': 1, 'B': 2, 'C': 3, 'D': 4}, name='AddedRow')

# Transposing the Series to fit as a new row in the DataFrame
extended_df = pd.concat([extended_df, new_series.to_frame().T])

print("Extended DataFrame after adding transposed Series:")
print(extended_df)
print("\n")

# Output:
# Extended DataFrame:
#    A   B   C    D
# 0  10  40  70  100
# 1  20  50  80  110    
# 2  30  60  90  120

# Extended DataFrame after adding transposed Series:
#            A   B   C    D
# 0       10  40  70  100
# 1       20  50  80  110
# 2       30  60  90  120
# AddedRow  1   2   3    4

# Please note how transposing the Series allows it to fit perfectly as a new row.
# The transposition converts the Series from a vertical format (which is the default for a Series) to a horizontal format that aligns with DataFrame rows.

