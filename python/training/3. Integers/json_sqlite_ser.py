import json
import sqlite3
import struct

def json_example():
    print("JSON Serialization/Deserialization Example")
    
    original_int = 42
    large_int = 34252345
    
    # Serialize to JSON
    json_data = json.dumps({"small_int": original_int, "large_int": large_int})
    print(f"Serialized JSON: {json_data}")
    
    # Show the byte representation of JSON
    json_bytes = json_data.encode('utf-8')
    print(f"JSON byte representation: {list(json_bytes)}")
    
    # Deserialize from JSON
    deserialized_data = json.loads(json_data)
    print(f"Deserialized data: {deserialized_data}")

def database_example():
    print("Database Storage/Retrieval Example")
    
    # Connect to an in-memory SQLite database
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Create a table and insert integers
    cursor.execute('CREATE TABLE numbers (value INTEGER)')
    small_int = 42
    large_int = 342523
    cursor.execute('INSERT INTO numbers (value) VALUES (?)', (small_int,))
    cursor.execute('INSERT INTO numbers (value) VALUES (?)', (large_int,))
    conn.commit()
    
    # Retrieve integers from the database
    cursor.execute('SELECT value FROM numbers')
    rows = cursor.fetchall()
    
    for row in rows:
        value = row[0]
        # Display the integer and its byte representation
        print(f"Retrieved integer: {value}")
        byte_representation = value.to_bytes((value.bit_length() + 7) // 8, byteorder='big') or b'\x00'
        print(f"Binary representation (SQLite): {byte_representation}")

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    json_example()
    database_example()
