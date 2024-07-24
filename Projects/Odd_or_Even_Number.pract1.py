# Is a Number Even or Odd Game

play_game = True


def is_even_or_odd(number):
    if number == 0:
        result = False
    else:
        result = bool(number % 2 == 0)
    return result


print("Wecome to: Is a Number Even or Odd Game")
print("Type 'q' to quit\n")

while play_game:

    user_number_str = input("Enter number to check if it is even or odd: ")

    if user_number_str == "q":
        play_game = False
    else:
        print("\t", is_even_or_odd(int(user_number_str)))
