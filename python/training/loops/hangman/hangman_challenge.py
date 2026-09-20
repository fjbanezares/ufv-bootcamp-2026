# Hangman Game Challenge
# Your task is to complete this Hangman game using the given hints and your understanding of Python.

from h_art import logo

# TODO-1: Import the word_list from hangman_words.py
from h_words import word_list

# TODO-2: Randomly choose a word from word_list.
chosen_word = None  # your code here
word_length = len(chosen_word)

# Initialize game conditions
end_of_game = False
lives = 6

print(logo)

# TODO-3: Create a display list filled with "_" placeholders for each letter in the chosen word.
display = None  # your code here

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # TODO-4: Check if the guessed letter was already guessed before.
    # your code here

    # TODO-5: Iterate over the chosen word to check if the guessed letter exists in it.
    # your code here

    # TODO-6: If guessed letter is not in the chosen_word, reduce lives.
    # your code here

    # Display the current status of guessed letter  s.
    print(f"{' '.join(display)}")

    # TODO-7: If there are no more "_" in display, user wins.
    # your code here

    # Display the current hangman stage (based on lives left).
    from h_art import stages
    print(stages[lives])
