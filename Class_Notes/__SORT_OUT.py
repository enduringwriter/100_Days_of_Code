college_years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
print(list(enumerate(college_years, 2019)))


fruits = ['Apples', 'Oranges', 'Bananas']
quantities = [5, 3, 4]
prices = [1.50, 2.25, 0.89]
i = 0
output = []
for fruit in fruits:
    temp_qty = quantities[i]
    temp_price = prices[i]
    output.append((fruit, temp_qty, temp_price))
    i += 1
print(output)

groceries = zip(fruits, quantities, prices)
print(groceries)
groceries_list = list(groceries)
print(groceries_list)


employee_numbers = [2, 9, 18, 28]
employee_names = ["Candice", "Ava", "Andrew", "Lucas"]
zipped_values = zip(employee_names, employee_numbers)
zipped_list = list(zipped_values)
print(zipped_list)


def print_alpha_nums(abc_list, num_list):
    for char in abc_list:
        for num in num_list:
            print(char, num)
    return
print_alpha_nums(['a', 'b', 'c'], [1, 2, 3])


my_set = {0, 'apple', 3.5}
print(my_set)


# Recursive Functions
def factorial(x):
    if x == 1:  # This is the base case
        return 1

    else:  # This is the recursive case
        return(x * factorial(x-1))
print(factorial(4))

# review this example
# https://libguides.ntu.edu.sg/python/recursivefunctions
def find_min(x_list, total):
    if total == 1:
        return x_list[0]

    else:
        print("b", total, x_list[total-1])
        return min(x_list[total-1], find_min(x_list, total-1))

A = [1, 4, 24, 17, -5, 10, -22]
total = len(A)

print(find_min(A, total))

def even_integer_generator(n):
    for number in range(n):
        if number % 2 == 0:
            yield number

print(list(even_integer_generator(10)))

import numpy as np
print(np.ones([1,2,3,4,5]))

t = {x for x in range(100) if x%3 == 0}
print(t)