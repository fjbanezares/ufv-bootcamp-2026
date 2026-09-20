import ctypes
import sys

# Define the structure for PyObject and PyLongObject using ctypes
class PyObject(ctypes.Structure):
    _fields_ = [("ob_refcnt", ctypes.c_ssize_t),  # Reference count (8 bytes on 64-bit systems)
                ("ob_type", ctypes.c_void_p)]     # Type pointer (8 bytes)

class PyLongObject(ctypes.Structure):
    _fields_ = [("ob_base", PyObject),            # Base object header
                ("ob_digit", ctypes.c_uint32 * 1)]  # First digit of the integer

def print_int_memory_layout(n):
    # Get the address of the integer object
    int_address = id(n)
    
    # Cast the address to a PyLongObject pointer
    int_obj = ctypes.cast(int_address, ctypes.POINTER(PyLongObject)).contents
    
    # Print the address and general information about the integer
    print(f"Memory layout of integer {n} (address: {int_address}):")
    print(f"Size of integer object: {sys.getsizeof(n)} bytes")

    # Calculate the number of bytes to print
    num_bytes = sys.getsizeof(n)
    
    # Print the raw bytes in memory
    print("Byte representation:")
    for i in range(num_bytes):
        byte = ctypes.cast(int_address + i, ctypes.POINTER(ctypes.c_ubyte)).contents.value
        print(f"Byte {i:2}: {byte:02x}")
    
    print("\n")
    
    # Print detailed breakdown of the header and value
    print(f"Reference count: {int_obj.ob_base.ob_refcnt}")
    print(f"Type pointer: {int_obj.ob_base.ob_type}")
    
    # Calculate the number of digits
    num_digits = (num_bytes - ctypes.sizeof(PyObject)) // ctypes.sizeof(ctypes.c_uint32)
    
    # Print each digit
    for i in range(num_digits):
        digit = ctypes.cast(int_address + ctypes.sizeof(PyObject) + i * ctypes.sizeof(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32)).contents.value
        print(f"Digit {i}: {digit}")
    
    print("\n")

# Example usage with small and large integers
small_int = 42
large_int = 34252345432534253543342

print_int_memory_layout(small_int)
print_int_memory_layout(large_int)
