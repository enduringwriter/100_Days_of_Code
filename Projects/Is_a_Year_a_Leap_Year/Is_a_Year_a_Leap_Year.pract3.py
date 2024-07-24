# Is a Year a Leap Year
# A leap year is evenly divisible by 4
# unless it is divisible by 100, except in the case where it is also divisible by 400
# play game and includes function

play_game = True


def check_for_leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0:
            print(f"\t{year} is a leap year.")
        elif year % 100 == 0 and year % 400 == 0:
            print(f"\t{year} is a leap year.")
        else:
            print(f"\t{year} is not a leap year.")
    else:
        print(f"\t{year} is not a leap year.")
    return


print("Is a Year a Leap Year\nType '0' to quit\n")

while play_game:
    year_input = int(input("Enter year: "))
    if year_input == 0:
        play_game = False
    else:
        check_for_leap_year(year=year_input)