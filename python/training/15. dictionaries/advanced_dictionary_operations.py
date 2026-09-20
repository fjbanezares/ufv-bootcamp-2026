import threading  # Importing threading module to handle multithreaded operations

# Function to update a dictionary using the 'update()' method
def demonstrate_update():
    dict1 = {"apple": "fruit", "broccoli": "vegetable", "chicken": "meat"}
    dict2 = {"banana": "fruit", "broccoli": "green vegetable"}  # 'broccoli' key will overlap

    # Merging dict2 into dict1 using the update() method
    dict1.update(dict2)
    print("After update():", dict1)  
    # Output: {'apple': 'fruit', 'broccoli': 'green vegetable', 'chicken': 'meat', 'banana': 'fruit'}

# Function to demonstrate shallow copy using 'copy()' method
def demonstrate_copy():
    dict1 = {"apple": "fruit", "broccoli": "vegetable"}
    
    # Creating a shallow copy of dict1
    dict3 = dict1.copy()

    print("Original dict:", dict1)  
    # Output: {'apple': 'fruit', 'broccoli': 'vegetable'}

    # Modifying dict3
    dict3["apple"] = "green fruit"
    print("After modifying copy, Original dict:", dict1)  
    # Output: {'apple': 'fruit', 'broccoli': 'vegetable'}
    print("Modified copy:", dict3)  
    # Output: {'apple': 'green fruit', 'broccoli': 'vegetable'}

# Function to simulate race conditions without using setdefault()
def update_dict_without_setdefault(shared_dict, key, value):
    # Checking if key exists in dictionary
    if key not in shared_dict:
        # If key does not exist, add key-value pair to dictionary
        shared_dict[key] = value

# Function to safely update a dictionary using 'setdefault()' to avoid race conditions
def update_dict_using_setdefault(shared_dict, key, value):
    # 'setdefault()' checks if the key exists and adds it if it doesn't in one atomic operation
    shared_dict.setdefault(key, value)

# Demonstrate race conditions using threads without 'setdefault()'
def demonstrate_race_condition_without_setdefault():
    print("\nDemonstrating race condition without setdefault()...")
    shared_dict = {"apple": "fruit"}  # Shared dictionary
    threads = []  # List to keep track of threads

    for i in range(5):
        # Creating a thread to update dictionary without using 'setdefault()'
        thread = threading.Thread(target=update_dict_without_setdefault, args=(shared_dict, f"key{i}", f"value{i}"))
        threads.append(thread)  # Adding thread to list
        thread.start()  # Starting thread

    # Ensuring all threads have finished executing
    for thread in threads:
        thread.join()

    print("Result without setdefault():", shared_dict)  
    # Output may vary due to race conditions

# Demonstrate safe dictionary updates using threads with 'setdefault()'
def demonstrate_safe_updates_with_setdefault():
    print("\nDemonstrating safe updates with setdefault()...")
    shared_dict = {"apple": "fruit"}  # Shared dictionary
    threads = []  # List to keep track of threads

    for i in range(5):
        # Creating a thread to update dictionary using 'setdefault()'
        thread = threading.Thread(target=update_dict_using_setdefault, args=(shared_dict, f"key{i}", f"value{i}"))
        threads.append(thread)  # Adding thread to list
        thread.start()  # Starting thread

    # Ensuring all threads have finished executing
    for thread in threads:
        thread.join()

    print("Result with setdefault():", shared_dict)  
    # Output will be consistent without race conditions

# Main function to demonstrate all concepts
def main():
    print("Demonstrating update() method...")
    demonstrate_update()
    print("\nDemonstrating copy() method...")
    demonstrate_copy()
    demonstrate_race_condition_without_setdefault()
    demonstrate_safe_updates_with_setdefault()

# Execute main function
if __name__ == "__main__":
    main()

    # PLEASE ensure you understand these methods to avoid issues in your Python programs.
    # THANK YOU for taking the time to learn about advanced dictionary operations in Python!
