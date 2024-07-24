# Is a Year a Leap Year
# A leap year is evenly divisible by 4
# unless it is divisible by 100, except in the case where it is also divisible by 400
# play game

play_game = True

print("Is a Year a Leap Year"
      "\nType '0' to quit\n")
while play_game:
    year = int(input("Enter year: "))
    if year == 0:
        play_game = False
    elif year % 4 == 0:
        if year % 100 != 0:
            print(f"{year} is a leap year.")
        elif year % 100 == 0 and year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is not a leap year.")

