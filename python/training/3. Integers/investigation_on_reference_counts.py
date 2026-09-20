import sys

def check_reference_counts():
    # Small integer (interned)
    small_int = 42
    print(f"Reference count of integer {small_int}: {sys.getrefcount(small_int) - 1}")

    # Large integer (not interned)
    large_int = 342523454325342535433423534534
    print(f"Reference count of integer {large_int}: {sys.getrefcount(large_int) - 1}")

    # Non-interned integer
    non_interned_int = 10006346436
    print(f"Reference count of integer {non_interned_int}: {sys.getrefcount(non_interned_int) - 1}")

# Call the function to check reference counts
check_reference_counts()
