import ctypes

# Function to print the memory layout of an integer
def print_int_memory_layout(n):
    # Get the address of the integer object
    int_address = id(n)
    # Create a ctypes pointer to the integer object
    int_obj = ctypes.cast(int_address, ctypes.POINTER(ctypes.py_object)).contents
    
    # Print the address and the first few bytes (header + value)
    print(f"Memory layout of integer {n} (address: {int_address}):")
    
    # Assume a 64-bit system, 8 bytes for header information
    for i in range(8 * 4):  # Print more bytes for larger integers
        byte = ctypes.cast(int_address + i, ctypes.POINTER(ctypes.c_ubyte)).contents.value
        print(f"Byte {i}: {byte:02x}")
        
    print("\n")

# Example usage with small and large integers
small_int = 42
large_int = 34252345432534253543342345345345354645364536345635624624356246423624662724574523764236524624624572572462462462472572457624462346

print_int_memory_layout(small_int)
print_int_memory_layout(large_int)
