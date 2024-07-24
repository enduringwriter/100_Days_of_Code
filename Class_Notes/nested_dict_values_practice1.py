####### MY EDITED VERSION
# Python3 code to demonstrate working of
# Maximum Value in Nested Dictionary
# Using loop
# EDITED
# initializing dictionary
test_dict = {'gfg': {'a': 15, 'b': 14},
             'is': {'d': 2, 'e': 10, 'f': 3},
             'best': {'g': 19}}

print("\tMY EDITED VERSION")

# printing original dictionary
print("The original dictionary: ", test_dict)

# Maximum Value in Nested Dictionary
# Using loop
a = {}
for key, val in test_dict.items():
    a[key] = max(val.values())

# printing result
print("The modified dictionary: ", a)



# https://www.geeksforgeeks.org/python-maximum-value-in-nested-dictionary/



####### ORIGINAL EXPANDED
# Python3 code to demonstrate working of
# Maximum Value in Nested Dictionary
# Using loop

# initializing dictionary
test_dict = {'gfg': {'a': 15, 'b': 14},
             'is': {'d': 2, 'e': 10, 'f': 3},
             'best': {'g': 19}}

print("\t ORIGINAL EXPANDED")

# printing original dictionary
print("The original dictionary: ", test_dict)

# Maximum Value in Nested Dictionary
# Using loop
b = {}
for key, val in test_dict.items():
    max_val = 0
    for ele in val.values():
        if ele > max_val:
            max_val = ele
    b[key] = max_val

# printing result
print("The modified dictionary: ", b)




###### ORIGINAL SIMPLIFIED
# Python3 code to demonstrate working of
# Maximum Value in Nested Dictionary
# Using max() + dictionary comprehension

# initializing dictionary
test_dict = {'gfg': {'a': 15, 'b': 14},
             'is': {'d': 2, 'e': 10, 'f': 3},
             'best': {'g': 19}}

print("\t ORIGINAL SIMPLIFIED")

# printing original dictionary
print("The original dictionary: ", test_dict)

# Maximum Value in Nested Dictionary
# Using max() + dictionary comprehension
c = {key: max(val.values()) for key, val in test_dict.items()}

# printing result
print("The modified dictionary: ", c)
