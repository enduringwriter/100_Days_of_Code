# Love Calculator, Variation 1 of the Love Calculator game
# Given two names, sum the total times a letter in each person's name matches a letter in "true love"
# The letter "e" does not count twice just because it is found in both "true" and "love"
# love_list is a string, match love letters by using set then join to convert the set list back to a string
# This time, calculate love scores separately, then add them at the end

play_game = True


def get_love_score(name_1_gls, name_2_gls):
    """
    Calculate love count for each name, and combine to get Love Score.
    :param name_1_gls: 4
    :param name_2_gls: 9
    :return: 13
    """
    # global love_count
    print(f"{name_1_original}'s love count is: {len(name_1_gls)}")
    print(f"{name_2_original}'s love count is: {name_2_gls}")
    love_score = len(name_1_gls) + name_2_gls
    print(f"Total love count: {love_score}")
    love_status(love_score=love_score)  # or call this function in the main code using global parameters
    return love_score


def love_status(love_score):
    """
    print love status that corresponds to love score
    :param love_score: 22
    :return: "You go together like honey on buns."
    """
    if 1 <= love_score <= 10 or love_score >= 70:
        print("You go together like cake and mentos.\n")
    if 30 <= love_score <= 50:
        print("You go together like honey on buns.\n")
    if 10 < love_score < 30 or 50 < love_score < 70:
        print("You go together like marshmallows.\n")
    else:
        print("")
    return


def get_unique_letters(name_1_gul, name_2_gul):
    """
    print unique "true love" letters found in both names
    :param name_1_gul: "etu"
    :param name_2_gul: "oolvevv"
    :return: "etuolv"
    """
    unique_love_letters_list = set(name_1_gul + name_2_gul)
    unique_love_letters = "".join(unique_love_letters_list)
    return print(f"Unique love letters are: {unique_love_letters}")


print("Welcome to the Love Calculator")
print("Enter your name and the person you like, and Love Calculator will give you a Love Score")
print("To exit game, type 'q'\n")

while play_game:

    # global love_count
    true_love = "truelove"
    name_2_love_count = 0
    name_2_love_letters = ""

    name_1_original = input("Enter name of person 1: ")
    name_1 = name_1_original.lower()
    if name_1 == "q":
        play_game = False
        break
    name_2_original = input("Enter name of person 2: ")
    name_2 = name_2_original.lower()
    if name_2 == "q":
        play_game = False
        break

    # get love count for name_1 - condensed for if loop
    name_1_love_letters_list = [letter for letter in name_1 if letter in true_love]
    name_1_love_letters = "".join(name_1_love_letters_list)

    # get love count for name_2 - expanded for if loop
    for letter in name_2:
        if letter in true_love:
            name_2_love_count += 1
            name_2_love_letters += letter

    get_unique_letters(name_1_gul=name_1_love_letters, name_2_gul=name_2_love_letters)

    get_love_score(name_1_gls=name_1_love_letters, name_2_gls=name_2_love_count)

    # love_status(love_score=love_count)  # if calling from here, use global parameters

# Note, the following code counts the letter "e" twice b/c it's a loop within a loop
    # for letter in name_2:
    #     # print("letter", letter)
    #     for x in true_love:
    #         # print("x:", x)
    #         if letter == x:
    #             # print("letter equals x")
    #             name_2_love_count += 1
    #             name_2_love_letters += letter
    #             # print("love letters: ", name_2_love_letters)
    #             # print(name_2_love_count)
