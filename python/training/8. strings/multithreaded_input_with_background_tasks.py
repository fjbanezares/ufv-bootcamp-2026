# multithreaded_input_with_background_tasks.py

import threading
import time

# Function to handle user input in a separate thread
def input_thread():
    # Please enter some input when prompted; this will block this thread only
    user_input = input("Input Thread: Please enter something: ")
    print(f"Input Thread: You entered: {user_input}")

# Function to simulate a background task
def background_task(name):
    for i in range(5):
        # Print the current task and iteration
        print(f"Background Task {name}: Working... {i + 1}/5")
        # Simulate some work by sleeping for a short time
        time.sleep(2)

def main():
    # Create a thread for handling user input
    input_t = threading.Thread(target=input_thread)
    
    # Create a list to hold background task threads
    background_threads = []

    # Create and start multiple background threads
    for i in range(3):
        # Create a new thread for each background task
        t = threading.Thread(target=background_task, args=(i,))
        # Add the thread to the list of background threads
        background_threads.append(t)
        # Start the background task thread
        t.start()

    # Start the input thread
    input_t.start()

    # Wait for all background threads to complete
    for t in background_threads:
        t.join()

    # After all background tasks are done, wait for the input thread to complete
    input_t.join()

    print("Main Thread: All tasks and input handling are complete. Thank you for your patience!")

if __name__ == "__main__":
    main()
