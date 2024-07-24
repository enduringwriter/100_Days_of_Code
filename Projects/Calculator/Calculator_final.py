# Calculator
# Learn to use dictionaries with functions
# Learn to pass function output

#### Method 1 - using 1 dictionary and 4 functions
#### Traditional method is shown at the very end of this file and uses 1 function and 4 conditions but no dictionary

# Create "calculator functions"
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# create variables
continue_calculating = True

# create a dictionary were key-value pair is the "operation":function that calls forth "calculator functions"
operations = {
    "+":add,
    "-":subtract,
    "*":multiply, 
    "/":divide
}
def calculator():
    # User inputs
    n1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    while continue_calculating: 
        # User input - another number
        operation = input("Pick an operation: ")
        n = float(input("What's the next number?: "))

        # Call function and Pass previous function ouput 
        calculation_function = operations[operation]
        answer = calculation_function(n1, n)
        ##BUG second_answer = calculation_function(calculation_function(n1, n2), n3)  #can't do this b/c the second operation will overwrite the first operation

        # Ouput solution w/ 3rd number
        print(f"{n1} {operation} {n} = {answer}")

        if input(f"Type 'y to continue calculating with {answer}, or type 'n' to exit.: ") == 'y':
            # Reasssign current answer
            n1 = answer
        else:
            continue_calculating == False
            break

calculator()    # call calculator function

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
# n1 = float(input("What's the first number? "))
# operation = input(("+ \n- \n* \n/ \n Pick an operation: "))
# n2 = float(input("What's the first number? "))

# Call function and output solution
# print(calculator(n1, n2, operation))
