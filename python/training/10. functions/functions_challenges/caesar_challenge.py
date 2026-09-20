# Caesar Cipher Challenge

# The goal of this challenge is to implement the Caesar Cipher, an ancient form of encryption.
# The user will input a direction (encode or decode), a message, and a shift value.
# Your task is to shift each letter of the message by the given shift value.
# If the shift goes beyond 'z', it should wrap around to the start of the alphabet.

# TODO: Define the alphabet list here. You might need to repeat it to handle shifts that exceed its length.

# TODO: Implement the caesar function that takes start_text, shift_amount, and cipher_direction as parameters.


def caesar(start_text, shift_amount, cipher_direction):
    pass  # You need to remove this pass statement and add your code here.


should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Ensure shift is within the range of the alphabet length. How can you do that?
    # TODO: Modify the shift here.

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
