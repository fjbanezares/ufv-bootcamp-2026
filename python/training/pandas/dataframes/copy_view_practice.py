import pandas as pd

# Creating a sample DataFrame
df = pd.DataFrame({
    'A': [1, 5, 9],
    'B': [2, 6, 10],
    'C': [3, 7, 11],
    'D': [4, 8, 12]
}, index=['a', 'b', 'c'])

print("Original DataFrame:")
print(df)
print("\n")

# 1. Direct Modification using .loc (Modifies the original DataFrame)
# -----------------------------------------------------------------------------
# This modifies the original DataFrame directly.
df.loc['a':'b', 'A'] = 10
print("After modifying rows 'a' to 'b' in column 'A' using .loc:")
print(df)
print("\n")

# 2. Avoiding Chained Indexing (Does NOT modify the original DataFrame)
# -----------------------------------------------------------------------------
# This line is an example of chained indexing which creates a copy and does not modify the original DataFrame.
# It triggers a SettingWithCopyWarning.
try:
    df.loc['a':'b']['A'] = 20
except pd.core.common.SettingWithCopyWarning as e:
    print("Caught SettingWithCopyWarning:", e)
print("After trying to modify using chained indexing (df.loc['a':'b']['A'] = 20):")
print(df)  # No change in original DataFrame
print("\n")

# Same as

try:
    df1 = df.loc['a':'b']; 
    df1['A']=10 # SettingWithCopy warning
except pd.core.common.SettingWithCopyWarning as e:
    print("Caught SettingWithCopyWarning:", e)
print("After trying to modify using chained indexing (df.loc['a':'b']['A'] = 20):")
print(df)  # No change in original DataFrame
print("\n")

# Proper way to modify with .loc in a single operation
df.loc['a':'b', 'A'] = 20
print("After correcting with single .loc operation (df.loc['a':'b', 'A'] = 20):")
print(df)
print("\n")

# 3. Using .at and .iat for Single Element Modification (Directly Modifies the original DataFrame)
# -----------------------------------------------------------------------------
# Using .at to modify a single element
df.at['b', 'C'] = 30
print("After modifying a single element using .at ('b', 'C'):")
print(df)
print("\n")

# Using .iat for integer location modification
df.iat[1, 2] = 40
print("After modifying a single element using .iat (1, 2):")
print(df)
print("\n")

# 4. Working with Copies Intentionally (Avoid SettingWithCopyWarning)
# -----------------------------------------------------------------------------
# When working with copies, explicitly use .copy() to avoid SettingWithCopyWarning.
df_copy = df.loc['a':'b', ['A', 'B']].copy()
df_copy['A'] = 50
print("Working on a copy:")
print(df_copy)
print("\n")

# No changes in the original DataFrame
print("Original DataFrame remains unchanged after modifying the copy!!:")
print(df)
print("\n")

# 5. Updating Original DataFrame from a Copy
# -----------------------------------------------------------------------------
# Now updating the original DataFrame with changes from the copy.
df.update(df_copy)
print("Original DataFrame after updating from the modified copy:")
print(df)
print("\n")

# 6. Explanation on Using .iloc and .loc with Slices
# -----------------------------------------------------------------------------
# When using .loc with slices, it returns a view or copy, which can be ambiguous. Use with care.
subset = df.loc['a':'b', ['A', 'B']]
print("Subset obtained using .loc (view or copy depending on the situation):")
print(subset)
print("\n")

subset['A']=11
print(subset)

print("\n")
print("How is the original:")
print(df)
print("\n")

print("How is the original after force update:")
df.update(subset)
print(df)
print("\n")


# To ensure a copy, explicitly use .copy()
subset_copy = df.loc['a':'b', ['A', 'B']].copy()
subset_copy['A'] = 60
print("Modified subset copy:")
print(subset_copy)
print("\n")

# 7. Suppressing SettingWithCopyWarning when modifying a copy
# -----------------------------------------------------------------------------
# Avoid SettingWithCopyWarning by ensuring you create a copy intentionally.
subset_safe = df.loc['a':'b', ['A', 'B']].copy()
subset_safe['B'] = 70  # This modification is safe and intentional
print("Modified safe copy:")
print(subset_safe)
print("\n")

print("Final state of the original DataFrame:")
print(df)
