# Number Guessing Game

import random

# variables
play_game = True
count_guesses_1 = 1
count_guesses_2 = 0  # add first guess


# generate random number
def get_random_number():
    random_number_int = random.randint(1, 100)
    return random_number_int


while play_game:

    print("Welcome to the Number Guessing Game")
    print("Enter q to quit at any time.\n")

    # get random number
    random_number = get_random_number()
    print(f"Hint, the random number is: {random_number}")

    # input user guess
    choice_str = input("Enter a number: ").lower()
    # analyze user guess
    # while not(1 <= int(choice_str) <= 100):
    if choice_str == 'q':
        play_game = False
        break
    elif isinstance(choice_str, str):
        print("Invalid entry. Please enter a number between 1 and 100.")
    elif not (1 <= int(choice_str) <= 100):
        print("Please enter a valid number between 1 and 100.")
    elif 1 <= int(choice_str) <= 100:
        # compare user guess with random number
        while int(choice_str) != random_number and (1 <= int(choice_str) <= 100):
            if int(choice_str) != random_number and int(choice_str) > random_number:
                print("You guessed too high.")
            elif int(choice_str) != random_number and int(choice_str) < random_number:
                print("You guessed too low.")
            elif int(choice_str) == random_number:
                print("You guessed correctly!")
                count_guesses = count_guesses_1 + count_guesses_2
                print(f"Total guesses: {count_guesses}")
                print("Would you like play again?")
                play_again = input("Press 'y' to continue. Any other key to quit. ").lower()
                if play_again == 'y':
                    play_game = True
                else:
                    play_game = False
            else:
                break
            count_guesses_2 += 1
            # choice_str = int(input("Enter a number: "))
            # while int(choice_str) != random_number and not (1 <= int(choice_str) <= 100):
            #     choice_str = int(input("Enter a number: "))
            # break
        # break
    # else:
    #     print("Something went wrong.")
    # choice_str = input("Enter a number: ").lower()
    # count_guesses_1 += 1
    continue
    # the following code is necessary if "continue" is not used and if "int()" is not used immediately above continue
    # if 1 <= int(choice_str) <= 100:
    #     choice = int(choice_str)  # valid choice "choice" allows game to continue
    #     break

    # output result when guess equals random number
