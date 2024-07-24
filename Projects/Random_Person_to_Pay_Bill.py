# Choose a random person to pay everybody's food bill

import random

# Input Names
# names_string = input("Give me everybody's names, separated by a comma. ")
names_string = "Angela, Ben, Jenny, Michael, Chloe"   # test run

# Split string names to a list of names
names = names_string.split(", ")

# Number of names in list
# total_names = len(names)    # total length is 5, which means total_names = 5. However, indexing begins with 0

# Random person chosen to pay the bill
# Solution using indexes and rand.int
# payer_index = random.randint(0, total_names - 1)     # subtract 1 because len value 5 would mean there are 6 people (0, 1, 2, 3, 4, 5)
# payer = names[payer_index]
# print(payer, "is going to buy the meal today!")


# Alternate solution using random.choice
print(random.choice(names), "is going to buy the meal today!")


# Alternate solution with for loop and random.choice
# for name in range(total_names):
#     payer = random.choice(names)
# print(payer, "is going to buy the meal today!")