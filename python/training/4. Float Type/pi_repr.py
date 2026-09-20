import struct
import decimal

def float_to_binary(num):
    # Pack the float into 8 bytes using big-endian format ('>d')
    packed = struct.pack('>d', num)
    # Unpack the 8 bytes into a 64-bit integer
    unpacked = struct.unpack('>Q', packed)[0]
    # Convert the 64-bit integer to a binary string
    binary = f'{unpacked:064b}'
    sign = binary[0]
    exponent = binary[1:12]
    mantissa = binary[12:]
    return sign, exponent, mantissa

def binary_to_decimal(binary_str):
    # Convert binary string to a decimal integer
    return int(binary_str, 2)

def binary_to_float(sign, exponent, mantissa):
    # Reconstruct the float from its binary components
    sign_int = int(sign)
    exponent_int = binary_to_decimal(exponent)
    mantissa_int = binary_to_decimal(mantissa)
    
    # Calculate the exponent value
    exponent_val = exponent_int - 1023
    
    # Calculate the mantissa value
    mantissa_val = 1 + sum(int(bit) * 2 ** -(i + 1) for i, bit in enumerate(mantissa))
    
    # Reconstruct the float value
    reconstructed_float = (-1) ** sign_int * mantissa_val * 2 ** exponent_val
    return reconstructed_float

def print_float_components(num):
    sign, exponent, mantissa = float_to_binary(num)
    print(f"Number: {num}")
    print(f"Sign bit: {sign} (0 means positive, 1 means negative)")
    print(f"Exponent (binary): {exponent} (decimal): {binary_to_decimal(exponent)}")
    print(f"Mantissa (binary): {mantissa}")
    print(f"Exponent value: {binary_to_decimal(exponent)} - 1023 = {binary_to_decimal(exponent) - 1023}")
    print(f"Mantissa value (as a binary fraction): 1.{mantissa}")
    
    reconstructed_float = binary_to_float(sign, exponent, mantissa)
    print(f"Reconstructed float: {reconstructed_float}")
    print(f"Imprecision: {abs(num - reconstructed_float)}")
    print()

print_float_components(3.14)
print_float_components(0.1 + 0.2)
print_float_components(0.1)
print_float_components(0.2)
