# Number Guessing Game Objectives:
# works correctly, but there is no play game again

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo
import os

# define fuction clear
def clear():
    os.system("clear")

#  global variables
TOTAL_ATTEMPTS = 5

# define fuction to compare guess with random number
def compare(random_numb, TOTAL_ATTEMPTS):
    # compare guess with random number
    # print(f"Pssst, the correct answer is {random_numb}")
    print(f"You have {TOTAL_ATTEMPTS} attempts remaining to guess the number.")
    while TOTAL_ATTEMPTS != 0:
        guess = int(input("\tMake a guess: "))
        if guess == random_numb:
            print(f"You guessed correctly! The answer was {random_numb}")
            break
        elif guess != random_numb:
            if guess > random_numb:
                print("Too high.")
            elif guess < random_numb:
                print("Too low.")
            elif guess == random_numb:
                print(f"You guessed correctly! The answer was {random_numb}")
                break
        TOTAL_ATTEMPTS -= 1
        print(f"You have {TOTAL_ATTEMPTS} attempts remaining to guess the number.")
    if TOTAL_ATTEMPTS == 0:
        print("You lose.")

# specify TOTAL_ATTEMPTS to user specification
def get_level(level):
    global TOTAL_ATTEMPTS
    if level == "easy":
        TOTAL_ATTEMPTS += 5
    else:
        TOTAL_ATTEMPTS
    return TOTAL_ATTEMPTS

def guessing_game():
    clear()
    print(logo)
    
    # generate random number
    random_numb = random.randint(1,100)

    # get level of difficulty
    level = input("Choose level of difficulty. Type 'easy' or 'hard': ")

    # call functions to play game
    get_level(level)
    compare(random_numb, total_attempts)

guessing_game()