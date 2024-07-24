# Password Generator

import random

# List of all possible password characters
uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"]

# Input password length, upper/lower case, numbers, and symbols from user
print("Welcome to Password Generator")
user_length = int(input("Please enter the length of your password. Minimum length is 8, max length is 18 "))
if user_length > 18 or user_length < 8:
    print("length must be between 8 and 18 charactors")
else:
    user_char_upper = int(input("How many uppercase letters would you like? "))
    user_char_lower = int(input("How many lowercase letters would you like? "))
    user_numb = int(input("How many numbers would you like? "))
    user_spec_char = int(input("How many special characters would you like? "))

# Verify password length. If correct, generate random variables per user specificiation
test_length = user_char_upper + user_char_lower + user_numb + user_spec_char
if test_length > 18 or test_length < 8:
    print("length must be between 8 and 18 charactors")
else:
    u = []
    l = []
    n = []
    sc = []
    for upper in range(0,user_char_upper):
        u.append(random.choice(uppercase))
    for lower in range(0,user_char_lower):
        l.append(random.choice(lowercase))
    for number in range(0,user_numb):
        n.append(str(random.choice(numbers)))
    for special_character in range(0,user_spec_char):
        sc.append(random.choice(symbols))

# Combine randomized lists (nested) 
password_total_lists = [u, l, n, sc]

# Convert nested list to one single list
password_single_list = sum(password_total_lists, [])

# Randomize password list and output solution
password_randomized = random.sample(password_single_list, k=user_length)

# Convert list to string and output solution
password = "".join(password_randomized)
print(f"New password is {password}")
