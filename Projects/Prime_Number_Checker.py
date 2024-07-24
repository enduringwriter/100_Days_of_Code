# Prime Number Checker

# Solution using loop
# def prime_checker(number):
#     if number > 1:
#     # Iterate from 2 to n/2
#         for i in range(2, int(number/2)+1):
#             # If number is divisible by any number between
#             # 2 and n/2, it is not prime
#             if (number % i) == 0:
#                 is_prime = False
#                 break
#         else:
#             is_prime = True
#     else:
#         is_prime = False
            
#     if is_prime == True:
#         print(number, "is a prime number")
#     else:
#         print(number, "is not a prime number")


# Solution using if conditions
def prime_checker(number):
    if number == 1:
        print("It's not a prime number.")
    if number == 2 or number == 3 or number == 5 or number == 7:
        print("It's a prime number.")
    elif number%2 == 0 or number%3 == 0 or number%4 == 0 or number%5 == 0 or number%6 == 0 or number%7 == 0 or number%8 == 0 or number%9 == 0:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")

n = int(input("Check if prime number: "))
prime_checker(number=n)


# #module not installed
# import sympy
# def prime_checker(number):
#     sympy.isprime(number)

# #mudule not installed
# from primePy import primes 
# def prime_checker(number):
#     primes.check(number)
