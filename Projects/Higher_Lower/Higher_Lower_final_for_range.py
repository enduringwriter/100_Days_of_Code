# Higher Lower Game using for x in range(0, total_cards) with break loop if guess is wrong

from clear_screen import clear
from art import logo, vs
from game_data import data
import random

# variables
total_score = 0

def get_random_card():
    return random.choice(data)

def format_card(card):
    name = card["name"]
    description = card["description"]
    country = card["country"]
    # test code, next 2 lines
    follower_count = card["follower_count"]
    print(f"Psst, hint: {name} has {follower_count} followers.")
    return f"{name} is a {description} from {country}"

def compare_card(guess):
    a_follower_count = card_a["follower_count"]
    b_follower_count = card_b["follower_count"]
    if (a_follower_count > b_follower_count and guess == "a") or (a_follower_count < b_follower_count and guess == "b"):
        return True
    else:
        return False

total_cards = len(data)

for x in range(0, total_cards):
    clear()
    print(logo)
    
    #get 2 random cards, but if both are equal, generate a new one
    card_a = get_random_card()
    card_b = get_random_card()
    if card_a == card_b:
        card_b = random.choice(data)

    # display cards to user
    print(format_card(card_a))
    print(vs)
    print(format_card(card_b))

    # output user current score and input user guess
    print(f"\nYou're current score: {total_score}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # count score
    score = sum([compare_card(guess)])
    if score == 1:
        total_score += score
    else:
        break
    x += 1
clear()
print(logo)
print(f"Game Over.\nFinal Score: {total_score}\n")

# this works correctly, but its not a loop with a condition to end the game. Also, it cycles through all elements after missing answer. Could be good to have final count of going through all items
# for x in range(3):
#     clear()
#     print(logo)
    
#     #get 2 random cards, but if both are equal, generate a new one
#     card_a = get_random_card()
#     card_b = get_random_card()
#     if card_a == card_b:
#         card_b = random.choice(data)

#     # display cards to user
#     print(format_card(card_a))
#     print(vs)
#     print(format_card(card_b))

#     # output user current score and input user guess
#     print(f"\nYou're current score: {total_score}")
#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()

#     # count score
#     score = sum([compare_card(guess)])
#     if score == 1:
#         total_score += score
#     print(f"Your final score is: {total_score}")
#     x += 1
