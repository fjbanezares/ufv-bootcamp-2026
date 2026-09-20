import ctypes
import sys

# Function to print the memory layout of an integer
def print_int_memory_layout(n):
    # Get the address of the integer object
    int_address = id(n)
    
    # Print general information about the integer
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

# Example usage with small and large integers
small_int = 42
large_int = 342523454325342535433423252356342346234626324623423423423564363

print_int_memory_layout(small_int)
print_int_memory_layout(large_int)
