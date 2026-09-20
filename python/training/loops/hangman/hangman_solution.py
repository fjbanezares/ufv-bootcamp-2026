# Import necessary libraries/modules
from h_art import logo  # Importing the logo for the hangman game from the h_art module.
import random  # The random module is used to generate random choices, specifically for selecting a random word from the word_list.

# Importing word_list which contains a list of possible words for the game.
from h_words import word_list

# Randomly selects a word from the word_list. This chosen_word will be what the player has to guess.
chosen_word = random.choice(word_list)

# Determines the length of the chosen word. This will help us keep track of how many letters need to be guessed.
word_length = len(chosen_word)

# Initialize game conditions:
# - end_of_game is a flag to determine whether the game is over (either the user has won or lost).
# - lives is the number of incorrect guesses allowed before the player loses the game.
end_of_game = False
lives = 6

# Print the game's logo at the start to provide a visual introsduction.
print(logo)

# Create a list called 'display' that initially contains "_" placeholders for each letter in the chosen_word.
# This will visually represent the user's progress, showing which letters have been correctly guessed.
display = ["_"] * word_length

# Main game loop; continues running until the game ends (either the user wins or loses).
while not end_of_game:
    # Prompt the user to guess a letter and convert it to lowercase to ensure consistency (since the chosen_word is likely lowercase).
    guess = input("Guess a letter: ").lower()

    # Check if the guessed letter was already guessed before (already present in 'display'). If so, inform the user.
    if guess in display:
        print(f"You've already guessed {guess}")

    # Now we loop over the letters of the chosen_word to check if the guessed letter matches any letter in the word.
    # Here's where we use `enumerate` to get both the index (position) and the letter from chosen_word.
    for position, letter in enumerate(chosen_word):
        # Debugging print: Shows the current position and the corresponding letter of the chosen_word.
        # This helps visualize how we are checking each position and its respective letter in the word.
        print(position, letter)

        # If the letter in the word matches the user's guess, we update the display at that position.
        if letter == guess:
            display[position] = letter

    # If the guessed letter is not found in the chosen_word, the user loses a life.
    # This makes the game harder as lives represent the number of mistakes allowed.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1  # Decrease the lives count when the guess is incorrect.
        if lives == 0:  # If no lives are left, the game ends with a loss.
            end_of_game = True
            print("You lose.")

    # Display the current status of the guessed letters. We join the display list into a string for easier visualization.
    print(f"{' '.join(display)}")

    # Check if there are no more "_" placeholders in the display list, meaning the user has guessed the entire word.
    if "_" not in display:
        end_of_game = True  # Game ends with a win.
        print("You win.")

    # Display the current hangman stage (visual representation of the hangman) based on the number of lives left.
    from h_art import stages
    print(stages[lives])
