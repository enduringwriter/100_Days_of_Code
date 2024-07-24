############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
from clear_screen import clear
from art_blackjack import logo
import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#Hint 6: Create a function called sum_cards that takes a List of cards as input i.e. the user's cards or the computer's cards
#and returns the score. 
#Look up the sum() function to help you do this.
def sum_cards(dealt_cards):
    """Take a list of cards and return the point value of the cards"""

    #Hint 7: Inside sum_cards() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(dealt_cards) == 21 and len(dealt_cards) == 2:
        return 0
    #Hint 8: Inside sum_cards() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in dealt_cards and sum(dealt_cards) > 21:
        dealt_cards.remove(11)
        dealt_cards.append(1)
    return sum(dealt_cards)

#Hint 13: Create a function called compare() and pass in the user_sum and computer_sum. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_sum is over 21, then the user loses. If the computer_sum is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_sum, computer_sum):
    #Bug fix. If you and the computer are both over, you lose.
    if user_sum > 21 and computer_sum > 21:
        return "You went over. You lose 😤"
    if user_sum == computer_sum:
        return "Draw 🙃"
    elif computer_sum == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_sum == 0:
        return "Win with a Blackjack 😎"
    elif user_sum > 21:
        return "You went over. You lose 😭"
    elif computer_sum > 21:
        return "Opponent went over. You win 😁"
    elif user_sum > computer_sum:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():

    print(logo)

    #Hint 5: Deal the user and computer 2 cards each using deal_card()
    user_cards = []
    computer_cards = []
    is_game_over = False

    # must use append to add single item to a list. Extend is for more than one item in a list. += is equivalent to .extend()
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

    while not is_game_over:
        #Hint 9: Call sum_cards(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        user_sum = sum_cards(user_cards)
        computer_sum = sum_cards(computer_cards)
        print(f"\tYour cards: {user_cards}, current hand value: {user_sum}")
        print(f"   Computer's face card: {computer_cards[1]}")

        if user_sum == 0 or computer_sum == 0 or user_sum > 21:
            is_game_over = True
        else:
            #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_sum != 0 and computer_sum < 17:
        computer_cards.append(deal_card())
        computer_sum = sum_cards(computer_cards)

    print(f"\tYour final hand: {user_cards}, final hand value: {user_sum}")
    print(f"   Computer's final hand: {computer_cards}, final hand value: {computer_sum}")
    print(compare(user_sum, computer_sum))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
