import signal
import time

# 🚀 Define a custom handler for SIGINT (usually triggered by Ctrl+C)
def custom_sigint_handler(signum, frame):
    print("🛑 Custom SIGINT handler triggered!")
    print(f"Signal Number: {signum}")  # Should be 2 for SIGINT
    print("Frame:", frame)  # The current stack frame where the signal was received
    # Custom actions can be added here, like saving state or logging
    print("✨ Exiting gracefully... Goodbye!")
    exit(0)  # Exit the program gracefully

# Register the custom handler for SIGINT
signal.signal(signal.SIGINT, custom_sigint_handler)

print("🔄 Program is running... Press Ctrl+C to trigger the custom SIGINT handler.")

# Simulate a long-running process
try:
    while True:
        print("💤 Sleeping... Press Ctrl+C to interrupt.")
        time.sleep(5)
except KeyboardInterrupt:
    # This block will not be executed because our custom handler will handle SIGINT
    print("⚠️ KeyboardInterrupt caught but won't execute due to custom handler.")

# 🧼 Additional cleanup code can go here if needed
print("🧼 Cleanup complete. Exiting program.")
