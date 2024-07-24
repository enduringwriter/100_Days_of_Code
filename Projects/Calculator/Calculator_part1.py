# Calculator
# Learn to use dictionaries with functions
# Learn to pass function output

#### Method 1 - using 1 dictionary and 4 functions
#### Traditional method is shown at the very end of this file and uses 1 function and 4 conditions but no dictionary

# Create functions to be called
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# create a dictionary were key-value pair is the "operation":function
operations = {
    "+":add,
    "-":subtract,
    "*":multiply, 
    "/":divide
}

# User inputs
n1 = int(input("What's the first number?: "))
n2 = int(input("What's the second number?: "))
for symbol in operations:
    print(symbol)
operation = input("Pick an operation: ")

# Call a function using "operations" dictionary
calculation_function = operations[operation]
first_answer = calculation_function(n1, n2)

# Output solution
print(f"{n1} {operation} {n2} = {first_answer}")

# User input - 3rd number
operation = input("Pick another operation: ")
n3 = int(input("What's the next number?: "))

# Call function and Pass previous function ouput 
calculation_function = operations[operation]
second_answer = calculation_function(first_answer, n3)
##BUG second_answer = calculation_function(calculation_function(n1, n2), n3)  #can't do this b/c the second operation will overwrite the first operation

# Ouput solution w/ 3rd number
print(f"{first_answer} {operation} {n3} = {second_answer}")



############################################################################
#### Traditional Method 2 - using 1 fuction and 4 if conditions
# def calculator(n1, n2, operation):
#     if operation == "+":
#         return n1 + n2
#     elif operation == "-":
#         return n1 - n2
#     elif operation == "*":
#         return n1 * n2
#     elif operation == "/":
#         return n1 / n2

# User inputs
# n1 = int(input("What's the first number? "))
# operation = input(("+ \n- \n* \n/ \n Pick an operation: "))
# n2 = int(input("What's the first number? "))

# Call function and output solution
# print(calculator(n1, n2, operation))




