############### Blackjack Project #####################


############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.


# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
import random


def deal_card():
    """Return a random card from deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # our deck of cards
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Return the score of users_card and computer_card """
    # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Hint 13: Create a function called compare() and pass in the user_score and computer_score.
# If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses.
# If the user has a blackjack (0), then the user wins.
# If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses.
# If none of the above, then the player with the highest score wins.


def compare(user_score, computer_score):
    if user_score == computer_score:
        return 'Draw'
    elif computer_score == 0:
        return 'loose opponent has blackjack'
    elif user_score == 0:
        return 'You Win ! '
    elif user_score > 21:
        return 'You loose '
    elif computer_score > 21:
        return 'Computer loose'
    elif user_score > computer_score:
        return 'User wins'
    else:
        return "Computer wins"

    # Hint 5: Deal the user and computer 2 cards each using deal_card() and append().


def play_game():
    user_cards = []
    computer_cards = []
    isgameOver = False
    for _ in range(2):
        new_card = deal_card()
        user_cards.append(new_card)
        computer_cards.append(new_card)
    # to update the score of both user and computer at every card drawn
    while not isgameOver:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Cards: {user_cards} and Your-Score: {user_score}")
        # only first card is shown
        print(f"Computer first card:{computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            isgameOver = True  # game is over
        else:
            # ask new card for user
            user_deal_card = input(
                "Type 'Y' to get another card or 'N' to pass: ")
            if user_deal_card == 'Y':
                user_cards.append(new_card)
                print(user_cards)
            else:
                isgameOver = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(new_card)
        # update computer_score for new-card
        computer_score = calculate_score(computer_cards)

    print(f" User final cards {user_cards} with score {user_score} ")
    print(
        f" Computer final cards {computer_cards} with score {computer_score}")
    print(compare(user_score, computer_score))
# DONE: Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# DONE : Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# DONE: Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


while input("Do you want to play the game type 'Y' ") == 'Y':
    play_game()
