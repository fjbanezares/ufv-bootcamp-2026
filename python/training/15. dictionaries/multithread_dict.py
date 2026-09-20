import threading

# Function to be executed in each thread
def update_dict(shared_dict, key, value):
    shared_dict[key] = value

# Shared dictionary to be updated by threads
shared_dict = {}
threads = []

# Create and start threads
for i in range(55):
    thread = threading.Thread(target=update_dict, args=(shared_dict, f"key{i}", f"value{i}"))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Print the shared dictionary
print(shared_dict)
