import signal
import os
import time
import random

# 🚀 Define a custom handler for SIGTERM (usually triggered by kill command)
def custom_sigterm_handler(signum, frame):
    print("🛑 Custom SIGTERM handler triggered!")
    print(f"Signal Number: {signum}")  # The signal number for SIGTERM is 15
    print("Frame:", frame)  # The current stack frame where the signal was received
    # Custom actions can be added here, like saving state or logging
    print("✨ Exiting gracefully... Goodbye!")
    exit(0)  # Exit the program gracefully

# 🚀 Define a custom handler for SIGHUP (hangup signal)
def custom_sighup_handler(signum, frame):
    print("🔄 Custom SIGHUP handler triggered!")
    print(f"Signal Number: {signum}")  # The signal number for SIGHUP is 1
    print("Frame:", frame)  # The current stack frame where the signal was received
    # Custom actions can be added here, like reloading configuration
    print("🔄 Reloading configuration...")

# Register the custom handlers
signal.signal(signal.SIGTERM, custom_sigterm_handler)
signal.signal(signal.SIGHUP, custom_sighup_handler)

print("🔄 Program is running...")

# Simulate a long-running process with probabilistic signal sending
try:
    for i in range(5):
        print("💤 Sleeping... Send SIGTERM, SIGHUP, or SIGKILL to interrupt.")
        time.sleep(1)
        # Introduce a 1/4 probability to send either SIGTERM or SIGHUP and a 1/3 probability to send SIGKILL
        rand_value = random.random()
        if rand_value < 0.25:
            print("🎲 Randomly sending SIGTERM...")
            os.kill(os.getpid(), signal.SIGTERM)
        elif rand_value < 0.5:
            print("🎲 Randomly sending SIGHUP...")
            os.kill(os.getpid(), signal.SIGHUP)
        elif rand_value < 0.75:
            print("🎲 Randomly sending SIGKILL...")
            # SIGKILL (signal number 9) is used to forcefully terminate the process
            # This signal cannot be caught or handled, and will immediately terminate the process
            os.kill(os.getpid(), signal.SIGKILL)
except KeyboardInterrupt:
    print("⚠️ KeyboardInterrupt caught. Exiting program.")

# 🧼 Additional cleanup code can go here if needed
print("🧼 Cleanup complete. Exiting program.")
