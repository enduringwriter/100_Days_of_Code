# Love Calculator, original love calculator
# Given two names, calculate their love score
# For each name, sum the number of times a letter in a name matches a letter in "true love"
# Convert counts into strings, add strings together to get a two-digit number, then convert back to an integer
# Learn: loops and conditions, calling a function, str and int conversion, play game until quit
# Learn: creating a list, converting list to string using .join, and getting unique letters in a string using set()
# Learn: matching elements using for and if loop versus .count, and defining matching elements as a function

play_love_game = True


# Calculate love count for each name, and combine to get Love Score.
def get_love_score(name_1_true_gls, name_1_love_gls, name_2_true_gls, name_2_love_gls):
    love_count_string_name_1 = str(len(name_1_true_gls)) + str(len(name_1_love_gls))
    love_count_string_name_2 = str(name_2_true_gls) + str(name_2_love_gls)
    love_score = int(love_count_string_name_1) + int(love_count_string_name_2)
    print(f"{name_1_original}'s love count is: {love_count_string_name_1}")
    print(f"{name_2_original}'s love count is: {love_count_string_name_2}")
    print(f"Your total love score is: {love_score}")
    love_status(love_score=love_score)
    return love_score


def love_status(love_score):
    """
    print love status that corresponds to love score
    :param love_score: 45
    :return: "You go together like honey on buns."
    """
    if 1 <= love_score <= 20 or love_score >= 75:
        print("You go together like cake and mentos.\n")
    if 30 <= love_score <= 55:
        print("You go together like honey on buns.\n")
    if 20 < love_score < 40 or 56 < love_score < 75:
        print("You go together like marshmallows.\n")
    else:
        print("")
    return


def get_unique_letters(name_1_true_gul, name_1_love_gul, name_2_true_gul, name_2_love_gul):
    """
    print unique "true love" letters found in both names
    :param name_1_true_gul: tu
    :param name_1_love_gul: ool
    :param name_2_true_gul: et
    :param name_2_love_gul: vol
    :return: tuolev
    """
    return print(f"Your love letters are: "
                 f"{''.join(set(name_1_true_gul + name_1_love_gul + name_2_true_gul + name_2_love_gul))}")


print("Welcome to the Love Calculator")
print("Enter your name and the person you like, and Love Calculator will give you a Love Score")
print("To exit game, type 'q'\n")

while play_love_game:

    true = "true"
    love = "love"
    name_2_true_letters = ""
    name_2_true_count = 0
    name_2_love_letters = ""
    name_2_love_count = 0

    name_1_original = input("Enter name of person 1: ")
    name_1 = name_1_original.lower()
    if name_1 == "q":
        play_love_game = False
        break
    name_2_original = input("Enter name of person 2: ")
    name_2 = name_2_original.lower()
    if name_2 == "q":
        play_love_game = False
        break

    # get "true" count of letters for name_1 - using condensed for if in a function
    def get_matched_items(str1, str2):
        matched_items = [letter for letter in str1 if letter in str2]
        return matched_items
    name_1_true_letters_list = get_matched_items(str1=name_1, str2=true)

    # get "love" count of letters for name_1 - using condensed for if
    name_1_true_letters = "".join(name_1_true_letters_list)

    name_1_love_letters_list = [letter for letter in name_1 if letter in love]
    name_1_love_letters = "".join(name_1_love_letters_list)

    # get "true love" counts for name_2 - expanded for if. Also, use .count() or len() for one of the counters.
    for letter in name_2:
        if letter in true:
            name_2_true_letters += letter
            name_2_true_count += 1
        if letter in love:
            name_2_love_letters += letter
            # name_2_love_count += 1
    name_2_love_count = name_2.count("l") + name_2.count("o") + name_2.count("v") + name_2.count("e")

    get_unique_letters(name_1_true_gul=name_1_true_letters, name_1_love_gul=name_1_love_letters,
                       name_2_true_gul=name_2_true_letters, name_2_love_gul=name_2_love_letters)

    get_love_score(name_1_true_gls=name_1_true_letters, name_1_love_gls=name_1_love_letters,
                   name_2_true_gls=name_2_true_count, name_2_love_gls=name_2_love_count)

    # love_status(love_score)
