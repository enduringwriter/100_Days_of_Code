# Is a Number Odd or Even

# Input User Information
user_number = int(input("Which number do you want to check? "))

# Condition and Output of Solution
if user_number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


def odd_even_number_b(number_list):
    even_list = [number for number in number_list if number % 2 == 0]
    odd_list = [number for number in number_list if number % 2 != 0]
    print(even_list, odd_list)
    return


odd_even_number_b([1, 2, 3, 4, 5])
odd_even_number_b([5])


def odd_even_number_a(number_list):
    even_list = []
    odd_list = []
    for number in number_list:
        if number % 2 == 0:
            even_list.append(number)
        elif number % 2 != 0:
            odd_list.append(number)
    print(even_list, odd_list)
    return


odd_even_number_a([1, 2, 3, 4, 5])
odd_even_number_a([5])


def is_odd_number(number):
    return print(True if number % 2 != 0 else False)


is_odd_number(5)