import os
import platform
import signal
import time

def handle_signal(signum, frame):
    print(f"Received signal {signum}")

if platform.system() == 'Windows':
    # Windows-specific signal handling
    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)
else:
    # POSIX-specific signal handling
    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)
    signal.signal(signal.SIGHUP, handle_signal)

print(f"Running on {platform.system()}... Press Ctrl+C to trigger SIGINT")

try:
    while True:
        print("Working...")
        time.sleep(1)
except KeyboardInterrupt:
    print("KeyboardInterrupt caught. Exiting gracefully.")
