# Heads or Tails
# learn randomization

import random

# generate random varaible
# random_side = random.randint(0,1)

# condition and output of solution
# Heads = 1 while Tails = 0
# if random_side == 1:
#     print("Heads")
# else:
#     print("Tails")


# condition and output of solution simplified
# print("Heads" if random.randint(0,1) == 1 else "Tails")


# User Input Conditions and Output of Solution
random_side = random.randint(0,1)

print("Welcome to the coin toss game.")
choose = input("Choose if you want \"Heads\" or \"Tails\" ").lower()
if choose == "heads":
    choose = 1
else:
    choose = 0

if random_side == 1 and choose == 1:
    print("Heads, you win!!!")
elif random_side == 1 and choose == 0:
    print("Heads, you lose.")
elif random_side == 0 and choose == 0:
    print("Tails, you win!!!")
else:
    print("Tails, you lose.")