# FizzBuzz game, 1 to 100
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

# def Fizz_Buzz_Game(n):
#     for number in range(1, n+1):
#         if number%15 == 0:
#             print("FizzBuzz")
#         elif number%5 == 0:
#             print("Buzz")
#         elif number%3 == 0:
#             print("Fizz")
#         else:
#             print(number)



# now instead of using number%3 == 0, a number is also divisible by 3 if the sum of all the digits in the number is divisible by 3
# writer a new FizzBuzz program using sum for numbers divisible by 3

# sum of a number divisible by 3
def get_sum_of_a_number(n):
    sum = 0
    while n != 0:
        sum += int(n % 10)
        n = int(n/10)
    if sum%3 == 0:
        return True
    else:
        return False

# test code
#  get_sum_of_a_number(n)

def Fizz_Buzz_Game(n):
    for number in range(1, n+1):
        if number%15 == 0:
            print("FizzBuzz")
        elif number%5 == 0:
            print("Buzz")
        elif get_sum_of_a_number(number) == True:
            print("Fizz")
        else:
            print(number)

Fizz_Buzz_Game(n=15)      # program works with string or number
