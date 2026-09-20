import json
import sqlite3
import sys
import ctypes

def print_memory_layout(n):
    """Prints the memory layout of an integer."""
    address = id(n)
    num_bytes = sys.getsizeof(n)
    byte_values = [ctypes.cast(address + i, ctypes.POINTER(ctypes.c_ubyte)).contents.value for i in range(num_bytes)]
    
    print(f"Integer value: {n}")
    print(f"Memory address: {address}")
    print(f"Memory size: {num_bytes} bytes")
    print(f"Byte values: {byte_values}")
    print("\n")

def json_example():
    print("JSON Serialization/Deserialization Example")
    
    original_int = 42
    print("Original integer:")
    print_memory_layout(original_int)
    
    # Serialize to JSON
    json_data = json.dumps(original_int)
    print(f"Serialized JSON: {json_data}")
    
    # Deserialize from JSON
    deserialized_int = json.loads(json_data)
    print("Deserialized integer:")
    print_memory_layout(deserialized_int)
    
def database_example():
    print("Database Storage/Retrieval Example")
    
    # Connect to an in-memory SQLite database
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Create a table and insert an integer
    cursor.execute('CREATE TABLE numbers (value INTEGER)')
    original_int = 57
    cursor.execute('INSERT INTO numbers (value) VALUES (?)', (original_int,))
    conn.commit()
    
    # Retrieve the integer from the database
    cursor.execute('SELECT value FROM numbers')
    row = cursor.fetchone()
    retrieved_int = row[0]
    
    print("Original integer:")
    print_memory_layout(original_int)
    
    print("Retrieved integer:")
    print_memory_layout(retrieved_int)
    
    # Close the database connection
    conn.close()

if __name__ == "__main__":
    json_example()
    database_example()
