import ctypes

# Define the structure for PyObject using ctypes
class PyObject(ctypes.Structure):
    _fields_ = [("ob_refcnt", ctypes.c_ssize_t),  # Reference count (8 bytes on 64-bit systems)
                ("ob_type", ctypes.c_void_p)]     # Type pointer (8 bytes)

def get_reference_count(n):
    # Get the address of the integer object
    int_address = id(n)
    
    # Cast the address to a PyObject pointer
    py_obj = ctypes.cast(int_address, ctypes.POINTER(PyObject)).contents
    
    # Return the reference count
    return py_obj.ob_refcnt

# Example usage with small and large integers
small_int = 42
large_int = 34252345432534253543342

# Print reference counts
print(f"Reference count of integer {small_int}: {get_reference_count(small_int)}")
print(f"Reference count of integer {large_int}: {get_reference_count(large_int)}")


import sys

def print_reference_count(n):
    # sys.getrefcount(n) returns the reference count of the object 'n'
    # It includes the temporary reference as an argument to getrefcount()
    ref_count = sys.getrefcount(n)
    # We subtract 1 from the reference count to get the actual count
    # This is because getrefcount() itself creates a temporary reference
    print(f"Reference count of integer {n}: {ref_count - 1}")

# Example usage with small and large integers
small_int = 42
large_int = 34252345432534253543342

# Print reference counts
print_reference_count(small_int)
print_reference_count(large_int)


# Additional test to demonstrate the difference with a non-interned integer
non_interned_int = 1000
print_reference_count(non_interned_int) 


# Additional test to demonstrate the difference with a non-interned integer
non_interned_int = 1000654
print_reference_count(non_interned_int)


import sys

def check_reference_counts():
    # Small integer (interned)
    small_int = 42
    print(f"Reference count of integer {small_int}: {sys.getrefcount(small_int) - 1}")

    # Large integer (not interned)
    large_int = 34252345432534253543342
    print(f"Reference count of integer {large_int}: {sys.getrefcount(large_int) - 1}")

    # Non-interned integer
    non_interned_int = 1000
    print(f"Reference count of integer {non_interned_int}: {sys.getrefcount(non_interned_int) - 1}")

# Call the function to check reference counts
check_reference_counts()

