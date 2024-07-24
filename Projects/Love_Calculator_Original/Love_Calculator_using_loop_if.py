# Love Calculator, Variation 2
# Learn Loop Conditions and Lowercase

# Input User Names
name_1 = input("What is your name? \n").lower()
name_2 = input("What is their name? \n").lower()

# Set Variables
count_love_word_1_name_1 = 0
count_love_word_2_name_1 = 0
count_love_word_1_name_2 = 0
count_love_word_2_name_2 = 0
love_score_tens_digit = 0
love_score_ones_digit = 0
love_score = 0

# Define Love Words
love_word_1 = "true"
love_word_2 = "love"

# Count Love Letters in Name_1
for letter in name_1:
    if letter in love_word_1:
        count_love_word_1_name_1 += 1
    if letter in love_word_2:
        count_love_word_2_name_1 += 1

# Count Love Letters in Name_2
for letter in name_2:
    if letter in love_word_1:
        count_love_word_1_name_2 += 1
    if letter in love_word_2:
        count_love_word_2_name_2 += 1

# Sum Love Letters in love-word_1 as tens digit and love-word_2 as ones digit
love_score_tens_digit = count_love_word_1_name_1 + count_love_word_1_name_2
love_score_ones_digit = count_love_word_2_name_1 + count_love_word_2_name_2

# Convert Love Letter Counts to 2-Digits Love Score
love_score = int(str(love_score_tens_digit) + str(love_score_ones_digit))

# Love Score
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like cake and mentos.")
elif 40 <= love_score <= 50:    # love_score between 40 and 50
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
