# Password Generator v2

import random

# List of all possible password characters
uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"]

# Input password length, upper/lower case, numbers, and symbols from user
print("Welcome to Password Generator")
user_length = int(input("Please enter the length of your password. Minimum length is 8, max length is 18 "))
user_uppercase = int(input("How many uppercase letters would you like? "))
user_lowercase = int(input("How many lowercase letters would you like? "))
user_number = int(input("How many numbers would you like? "))
user_specical_character = int(input("How many special characters would you like? "))

# Random uppercase letters
random_uppercase = ""
for character in range(0, user_uppercase):
    random_uppercase += random.choice(uppercase)
print(random_uppercase)

# Random lower letters
random_lowercase = ""
for character in range(0, user_lowercase):
    random_lowercase += random.choice(lowercase)
print(random_lowercase)

# Random numbers
random_number = ""
for character in range(0, user_number):
    random_number += str(random.choice(numbers))
print(random_number)

# Random special characters
random_special_character = ""
for character in range(0, user_specical_character):
    random_special_character += random.choice(special_characters)
print(random_special_character)

#Combine each random segment
random_combined = random_uppercase + random_lowercase + random_number + random_special_character
print(random_combined)
print(type(random_combined))

#Randomize the combined password
password = "".join(random.sample(random_combined, user_length))
print(f"Your password is: {password}")
print(type(password))


#
# The above random segments can be simplified by adding segments to the variable itself as follows
#


# Random uppercase letters
password = ""
for character in range(0, user_uppercase):
    password += random.choice(uppercase)
print(password)

# Random lower letters
for character in range(0, user_lowercase):
    password += random.choice(lowercase)
print(password)

# Random numbers
for character in range(0, user_number):
    password += str(random.choice(numbers))
print(password)

# Random special characters
for character in range(0, user_specical_character):
    password += random.choice(special_characters)
print(password)

print(type(password))

# Randomize the password
random_password = "".join(random.sample(password, user_length))
print(f"Your password is: {random_password}")
print(type(random_password))

# 
# Another solution is to set the password as a list [] rather than as a string ""
# 

password = []
for character in range(0, user_uppercase):
    password.append(random.choice(uppercase))   # can use += or .append(). Note that append() does not work with strings
print(password)

# Random lower letters
for character in range(0, user_lowercase):
    password += random.choice(lowercase)
print(password)

# Random numbers
for character in range(0, user_number):
    password += str(random.choice(numbers))
print(password)

# Random special characters
for character in range(0, user_specical_character):
    password += random.choice(special_characters)
print(password)

# Randomize the password
random.shuffle(password)
print(password)
print(type(password))

# Convert password list to string
random_password = ""
for character in password:
    random_password += character
print(f"Your password is: {random_password}")
print(type(random_password))

#
# another way of rearranging, but it does not use random module
#
xpassword = ['B', "7", "r", "(", "w"]
print(xpassword)
order = [3, 2, 0, 1, 4]
xpassword = [xpassword[i] for i in order]
print(xpassword)
print(type(xpassword))