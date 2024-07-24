from game_data import data
import random
from art import logo, vs
from clear_screen import clear

def get_random_card():
    return random.choice(data)

def format_card(card):
    """Extract only certain details from card: name, description, and country"""
    name = card["name"]
    description = card["description"]
    country = card["country"]
    # Test code
    # followers = card["follower_count"]
    # print(f"Pssst, the solution is: {name} has {followers} followers")
    # print(f'{name}: ')    
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess 
    and returns True if they got it right.
    Or False if they got it wrong.""" 
    if (a_followers > b_followers and guess == "a") or (b_followers > a_followers and guess == "b"):
        return True
    else:
        return False

def game():
    print(logo)
    score = 0
    game_should_continue = True
    card_a = get_random_card()
    card_b = get_random_card()

    while game_should_continue:
        card_a = card_b
        card_b = get_random_card()
      
        while card_a == card_b:
            card_b = get_random_card()

        print(f"Compare A: {format_card(card_a)}.")
        print(vs)
        print(f"Against B: {format_card(card_b)}.")
    
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = card_a["follower_count"]
        b_follower_count = card_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()

'''

FAQ: Why does choice B always become choice A in every round, even when A had more followers? 

Suppose you just started the game and you are comparing the followers of A - Instagram (364k) to B - Selena Gomez (174k). Instagram has more followers, so choice A is correct. However, the subsequent comparison should be between Selena Gomez (the new A) and someone else. The reason is that everything in our list has fewer followers than Instagram. If we were to keep Instagram as part of the comparison (as choice A) then Instagram would stay there for the rest of the game. This would be quite boring. By swapping choice B for A each round, we avoid a situation where the number of followers of choice A keeps going up over the course of the game. Hope that makes sense :-)

'''



# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.