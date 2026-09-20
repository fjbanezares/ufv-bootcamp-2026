# 🚀 Demonstration of KeyboardInterrupt and Infinite Loops

import time

def infinite_loop():
    print("Starting infinite_loop() - This will run indefinitely until interrupted.")
    while True:
        # Perform some operation to consume CPU
        _ = 2 ** 8
        # Simulate a small delay to show it's running
        time.sleep(0.1)

# Running the infinite loop and manually interrupting it
try:
    infinite_loop()
except KeyboardInterrupt:
    print("⏹️ Infinite loop stopped with KeyboardInterrupt (Ctrl+C).")

# Exploring long-running loops that consume CPU
def long_running_loop():
    print("Starting long_running_loop() - This loop will run many iterations.")
    for _ in range(10**9):
        # Perform some operation to consume CPU
        _ = 2 ** 8
    print("✅ Long-running loop finished.")

# Running the long loop
try:
    long_running_loop()
except KeyboardInterrupt:
    print("⏹️ Long-running loop stopped with KeyboardInterrupt (Ctrl+C).")
