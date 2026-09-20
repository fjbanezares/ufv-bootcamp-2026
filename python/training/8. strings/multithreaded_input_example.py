# multithreaded_input_example.py

import threading
import time

def thread_function(name):
    # Simulate some processing time
    time.sleep(1)
    # Please note: The following input() call will block this thread until the user provides input.
    user_input = input(f"Thread {name}: Please enter something: ")
    print(f"Thread {name} received input: {user_input}")

def main():
    # Create several threads
    threads = []
    for i in range(3):
        t = threading.Thread(target=thread_function, args=(i,))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print("All threads have finished execution.")

if __name__ == "__main__":
    main()
