# Is a Given Year a Leap Year
# Learn Nested If Else Elif Conditions

# Input User Information
year = int(input("Which year do you want to check? "))

# Condition and Output of Solution
# if year%4 == 0:
#     if year%100 == 0 and year%400 == 0:
#         print("Leap year.")
#     elif year%100 == 0 and year%400 != 0:
#         print("Not leap year")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")

# Condition and Output of Alternative Solution
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")