# Alphabet repeated twice to handle shifts that exceed the length of the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    """Cipher or Decipher a given text based on Caesar's encryption method."""
    end_text = ""

    # If the direction is decode, the shift amount becomes negative for the reverse shift
    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        # If the character is in the alphabet, shift it
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        # If it's not a letter, keep it as it is
        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")


should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Typencodee the shift number:\n"))

    # Taking the modulus to ensure shift is within the range of the alphabet length
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
