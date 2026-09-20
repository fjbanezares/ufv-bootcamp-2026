# 🚀 Let's explore how functions in conditions are executed and evaluated!

def always_true():
    print("Running always_true()")
    return True

def always_false():
    print("Running always_false()")
    return False

def infinite_loop():
    print("Running infinite_loop() - This will hang forever!")
    while True:
        pass

# Function executed and result is truthy
if always_true():
    print("✨ This will always print because always_true() returns True.")

# Function executed and result is falsy
if always_false():
    print("🚫 This will never print because always_false() returns False.")
else:
    print("✨ This will print because always_false() returns False.")

# Beware of infinite loops!
try:
    # Uncomment the next line to see the infinite loop in action
    #if infinite_loop():
      #  print("🚫 This will never print because infinite_loop() never returns.")
    pass
except KeyboardInterrupt:
    print("⏹️ Stopped the infinite loop with a KeyboardInterrupt.")

# Exploring truthy and falsy return values:d
def truthy_value():
    print("Returning a non-empty list, which is truthy.")
    return [1, 2, 3]

def falsy_value():
    print("Returning an empty list, which is falsy.")
    return []

if truthy_value():
    print("✨ This will print because the function returned a truthy value.")

if falsy_value():
    print("🚫 This will never print because the function returned a falsy value.")
else:
    print("✨ This will print because the function returned a falsy value.")
