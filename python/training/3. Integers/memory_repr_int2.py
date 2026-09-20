import ctypes
import sys

class PyObject(ctypes.Structure):
    _fields_ = [("ob_refcnt", ctypes.c_long),  # Reference count
                ("ob_type", ctypes.c_void_p)]  # Type pointer

class PyLongObject(PyObject):
    _fields_ = [("ob_digit", ctypes.c_long * 1)]  # At least one digit

def print_int_memory_layout(n):
    # Get the address of the integer object
    int_address = id(n)
    
    # Create a ctypes pointer to the PyLongObject
    int_obj = ctypes.cast(int_address, ctypes.POINTER(PyLongObject)).contents
    
    # Print the address and the first few fields
    print(f"Memory layout of integer {n} (address: {int_address}):")
    print(f"Reference count: {int_obj.ob_refcnt}")
    print(f"Type pointer: {int_obj.ob_type}")
    
    # Calculate number of digits
    num_digits = (sys.getsizeof(n) - ctypes.sizeof(PyObject)) // ctypes.sizeof(ctypes.c_long)
    
    # Print each digit
    for i in range(num_digits):
        digit = ctypes.cast(int_address + ctypes.sizeof(PyObject) + i * ctypes.sizeof(ctypes.c_long), ctypes.POINTER(ctypes.c_long)).contents.value
        print(f"Digit {i}: {digit}")
    
    print("\n")

# Example usage with small and large integers
small_int = 42
large_int = 34252345432534253543342

print_int_memory_layout(small_int)
print_int_memory_layout(large_int)
