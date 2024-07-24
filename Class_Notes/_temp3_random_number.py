# Number Guessing Game

import random

# variables
play_game = True


# generate random number
def get_random_number():
    random_number_int = random.randint(1, 100)
    return random_number_int


while play_game:
    # variables
    choice = int
    count_guesses = 1

    print("Welcome to the Number Guessing Game")
    print("Enter q to quit at any time.\n")

    # get random number
    random_number = get_random_number()
    print(f"Random number is {random_number}")

    # get user input
    choice_str = input("Enter a number: ").lower()
    if choice_str == 'q':
        play_game = False
        break
    elif choice == int:
        choice = int(choice_str)
    else:
        print("Please enter a valid entry: ")
        play_game = False

    # compare user choice with random number
    while choice != random_number:
        if choice != random_number and choice > random_number:
            print("You guessed too high.")
            choice = int(input("Enter a number: "))
        elif choice != random_number and choice < random_number:
            print("You guessed too low.")
            choice = int(input("Enter a number: "))
        else:
            print("Something went wrong!")
        count_guesses += 1

    if choice == random_number:
        print("You guessed correctly!")
        print(f"Total guesses: {count_guesses}")
        play_again = input("Play again? Y/N").lower()
        if play_again == 'y':
            play_game = True
        else:
            play_game = False
