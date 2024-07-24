# Love Calculator, Variation 2
# Learn Conditions Count and Lowercase

# Input User Names and Combine Strings
name_1 = input("What is your name? \n").lower()     # could use upper() or casefold()
name_2 = input("What is their name? \n").lower()
name = name_1 + name_2

# Count Unique Letters "true" and "love" in name
count_of_love_word_1 = name.count("t") + name.count("r") + name.count("u") + name.count("e")
count_of_love_word_2 = name.count("l") + name.count("o") + name.count("v") + name.count("e")

# Convert "true" and "love" Count to a 2-Digit Love Score
love_score = int(str(count_of_love_word_1) + str(count_of_love_word_2))

# Love Score Analysis
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like cake and mentos.")
elif love_score >= 40 and love_score <= 50:    # love_score between 40 and 50
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")