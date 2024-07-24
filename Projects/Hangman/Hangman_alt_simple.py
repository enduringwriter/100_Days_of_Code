# Hangman Variation
# User has a specified number of tries to guess the word without penalty of hangman
# Afer free guesses, Hangman begins on the 7th incorrect guess

import random

# Word list to choose from
word_list = ["ardvark", "baboon", "camel"]

# Randomly choose a word from the word_list
chosen_word = random.choice(word_list)

# Variables
word_length = len(chosen_word)
unique_word_length = len(set(chosen_word))
number_of_guesses = unique_word_length + 7

# Hangman ASCII Art, 7 stages, stages[0] is beginning stage, stages[6] is final stage
# Stages reverse order from origal list
# stages = ['''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========
# ''','''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''']

# analyze program given solution
# print("\n" + f"Pssst, the solution is: {chosen_word}")
# print(type(chosen_word))

# Display underscores corresponding to the number of letters in the random word
display = []
for letter in range(0, word_length):
    display += "_"
print(display, end="\n"*2)

# analzye condition of guess as "right" or "wrong"
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")
# print(display)

# Set counter and ouput count to user
count = number_of_guesses
print(f"You have {count} tries to guess the word")

# Code, Part 1 - Compare user guess with letters in chosen_word
while display != chosen_word and count != 0:   
    # Input user guess
    guess = input("Guess a letter: ").lower()
    
    # begin countdown of number_of_guesses
    count -= 1
    
    # Determine if user guess matches letter in chosen_word
    for letter in range(word_length):
        if guess == chosen_word[letter]:
            # print(f"guess is correct: {guess}")  ## analysis of condition
            display[letter] = chosen_word[letter]   
    
    # Output display whether guess is correct or incorrect
    print(display)
    
    # If user guesses before countdown, break loop to go to next code segment
    if "_" not in display:
        break
    
    # If user doesn't guess word correctly on last guess, break loop to avoid printing "You have 0 guesses remaining."
    if count == 0:
        break

    # Output total gueses remaining, if user has not solved the word
    print(f"You have {count} guesses remaining.")

# Code, Part 2 - Compare user word to chosen_word
# Convert list to string
display_final = "".join(display)
chosen_word_final = "".join(chosen_word)

# Output result
if display_final == chosen_word_final:
    print("You won!")
else:
    print("You lose")
