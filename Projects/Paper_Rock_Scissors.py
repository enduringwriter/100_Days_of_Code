# Paper Rock Scissors
# Rock = 0, Paper = 1, Scissors = 3

import random

# Input user choice
user_choice = int(input("What do you choose?\n\t Type 0 for Rock\n\t 1 for Paper\n\t 2 for Scissors\n"))

# Generate random computer choice
computer_choice = random.randint(0,2)

# Print user and computer choice
print(f"You chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

# Condition
if user_choice == computer_choice:
    print("It's a draw")
elif user_choice == 0 and computer_choice == 1:
    print("Computer wins")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 1 and computer_choice == 2:
    print("Computer wins")
elif user_choice == 2 and computer_choice == 0:
    print("Computer wins")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
else:
    print("You typed an invalid number, you lose!")


# Alternate Solution Simplified
# if computer_choice == user_choice:
#   print("It's a draw")
# elif user_choice == 0 and computer_choice == 2:
#   print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#   print("You lose")
# elif computer_choice > user_choice:
#   print("You lose")
# elif user_choice > computer_choice:
#   print("You win!")
# elif user_choice >= 3 or user_choice < 0: 
#   print("You typed an invalid number, you lose!")
