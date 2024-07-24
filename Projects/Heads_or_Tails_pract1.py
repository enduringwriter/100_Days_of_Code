# Heads or Tails game
# heads is assigned a value of 1 and tails 0
# play game

import random

play_game = True
total_plays = 0
win_count = 0

while play_game:
    total_plays += 1
    player_guess = input("Enter 'h' for heads or 't' for tails, or any other key to quit: ").lower()
    if player_guess == "h":
        player_guess = 1
    elif player_guess == "t":
        player_guess = 0
    else:
        play_game = False

    random_number = random.randint(0, 1)
    if player_guess == random_number:
        win_count += 1
    if player_guess == random_number and random_number == 1:
        print("\tHeads, you win!")
    elif player_guess == random_number and random_number == 0:
        print("\tTails, you win!")
    elif player_guess != random_number and random_number == 1:
        print("\tHeads, you lose.")
    else:
        print("\tTails, you lose.")

    print(f"\tYour score is {win_count}/{total_plays}")
