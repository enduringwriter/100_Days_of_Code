# Higher Lower Game using for x in range(0, total_cards) with break loop if guess is wrong

from clear_screen import clear
from art import logo, vs
from game_data import data
import random

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

def compare_card(guess, a_follower_count, b_follower_count):
    if (a_follower_count > b_follower_count and guess == "a") or (a_follower_count < b_follower_count and guess == "b"):
        return True
    else:
        return False

total_cards = len(data)

# total_score = 0 # if defining variable to be modified in game(), must declare it as global

def game():
    clear()
    print(logo)
    game_should_continue = True
    
    # global total_score

    total_score = 0

    while game_should_continue == True:
        
        #get 2 random cards, but if both are equal, generate a new one
        card_a = get_random_card()
        card_b = get_random_card()
        if card_a == card_b:
            card_b = random.choice(data)

        # display cards to user
        print(format_card(card_a))
        print(vs)
        print(format_card(card_b))

        # input user guess
        guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = card_a["follower_count"]
        b_follower_count = card_b["follower_count"]
        clear()
        print(logo)
        # count score
        score = sum([compare_card(guess, a_follower_count, b_follower_count)])
        if score == 1:
            total_score += score
            print(f"You're right! Current score: {total_score}\n")
        else:
            game_should_continue = False
            print(f"Final score: {total_score}\n")
    
game()