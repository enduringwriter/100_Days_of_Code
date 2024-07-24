# Hangman Game
# User has 7 guesses to guess the word
# An incorrect guess begins the process of hangman

import random

# import word_list and logo from files
# 7 stages, stages[0] is end stage, stages[6] is first stage. Logo and stages are ASCII Art
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

# Randomly choose a word from the word_list
chosen_word = random.choice(word_list)

# Variables
word_length = len(chosen_word)
number_of_guesses = 7  #counts from 6 to 0
end_of_game = False

# Testing code
# print(f"Psst, the solution is {chosen_word}")

# Display underscores corresponding to the number of letters in the random word
display = []
for _ in range(0, word_length):
    display += "_"
print(f"{' '.join(display)}", end="\n"*2)

# Output initial number of guesses
print(f"You have {number_of_guesses} guesses to guess the word")    # displays 7, 6, 5, 4, 3, 2, 1 to user

# Code - Hangman Game
while not end_of_game: 
    # Input user guess
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
      print(f"You already guessed {guess}")

    # Compare user guess to letter in chosen_word
    for letter in range(word_length):
        if guess == chosen_word[letter]:
            display[letter] = chosen_word[letter]
 
    # Begin hangman
    if guess not in chosen_word:
      print(f"{guess} is not in the word.")
      number_of_guesses -= 1
      if number_of_guesses == 0:
          end_of_game = True
          print(stages[0])
          print("You lose.")
          break

    # Output display
    print(f"{' '.join(display)}")
    
    # If user guesses before countdown, break loop to go to next code segment
    if "_" not in display:
        end_of_game = True
        print("You win!")
        break
    
    # Print hangman stage
    print(stages[number_of_guesses])

    # Output total gueses remaining, if user has not solved the word
    print(f"You have {number_of_guesses} guesses remaining.")