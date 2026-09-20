import pandas as pd

# Creating a sample DataFrame
df = pd.DataFrame({
    'A': [1, 4],
    'B': [2, 5],
    'C': [3, 6]
}, index=['a', 'b'])

print("Original DataFrame:")
print(df)
print("\n")

# New row data
new_row = pd.Series({'A': 7, 'B': 8, 'C': 9}, name='c')

# Method to insert a row at index position 1 (between existing indices 'a' and 'b')
# We will use slicing and pd.concat

# Step 1: Slice the DataFrame before the insertion point
df_before = df.iloc[:1]

# Step 2: Slice the DataFrame after the insertion point
df_after = df.iloc[1:]

# Step 3: Concatenate the slices with the new row
df_new = pd.concat([df_before, new_row.to_frame().T, df_after])

print("DataFrame after inserting a new row 'c':")
print(df_new)
print("\n")

