############### Blackjack Project #####################

# This project involves creating a simple game of Blackjack.
# There are different levels of difficulty based on the hints provided.

# The house rules for this version of Blackjack are outlined below:
# - The deck is unlimited in size, meaning cards are not removed as they're drawn.
# - There are no jokers in this game.
# - Face cards (Jack, Queen, King) all have a value of 10.
# - The Ace can be valued at either 11 or 1, depending on the total score.
# - The cards list provided below represents the deck. Each card has an equal chance of being drawn.

# Import necessary libraries
import random
import os
from art import logo

# Clear the console


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# This function returns a random card from the deck.


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# This function calculates the score of the cards list provided.
# It also handles the special cases of Blackjack and the value of the Ace card.


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards."""
    # A blackjack is an ace and a 10-card. It's represented as 0.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # If the total score exceeds 21 and there's an ace in the hand, replace the ace (11) with a 1.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# This function compares the scores of the user and the computer to determine the winner.


def compare(user_score, computer_score):
    """Compare user and computer scores and return the result."""
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

# This function encapsulates the entire game logic.


def play_game():
    """Play a game of Blackjack."""
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Initially, deal 2 cards each to the user and the computer.
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # The game continues until the user decides to stop or someone gets a blackjack or goes over 21.
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"   Computer's final hand: {computer_cards}, final score: {computer_score}"
    )
    print(compare(user_score, computer_score))


# The game can be played multiple times until the user decides to quit.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()

'''Using the variable name cards in multiple places can introduce confusion and potentially lead to bugs in several ways:

Ambiguity in Scope: Variables in Python have a concept of scope (e.g., local, global). If a variable named cards is defined both inside a function (local scope) and outside the function (global scope), there might be confusion about which variable is being referenced at different points in the code.
Mental Overhead: When reading or maintaining the code, a developer would need to constantly discern which cards is being referred to. This introduces unnecessary cognitive load.
Unintended Side Effects: If a function modifies a global cards when it was intended to work with a local cards, or vice versa, this can lead to unintended side effects that might be hard to debug.
Reduced Readability: Using the same name for different purposes reduces the readability of the code. Distinct names make the code self-explanatory, thereby reducing the need for additional comments.
Loss of Semantic Meaning: Variable names should be descriptive enough to convey their purpose or the kind of data they hold. If cards is used to refer to a deck in one place, a hand in another, and perhaps discarded cards somewhere else, it loses its semantic meaning, making the code harder to follow.
Refactoring Risks: If there's a need to refactor or modify the code, the presence of the same variable name in multiple places increases the risk of inadvertently changing something that wasn't intended to be changed.
External Libraries/Modules: If using external libraries or modules, there's a risk that one of them might also use a variable named cards. This can lead to namespace clashes and unexpected behaviors.

To avoid these issues, it's a best practice to use descriptive variable names that are specific to their purpose. For instance, instead of cards, use deck, player_hand, discarded_cards, etc., to be more explicit about the intended use and data each variable holds.'''
