# string and re modules for case

import string
import re
# this file access another file: open('/Users/keithstateson/DS_Py_101/Class_Notes/Test_Hello_Case.txt', 'r')

state = 'Texas'
nation = 'USA'
olympic_sport = 'world cup'
book = "it's not DIFFICULT to lEArn 10a pythoN"

print(f"original strings - state, nation, olympic sport: {state}, {nation}, {olympic_sport}")
print(state.upper())
print(nation.lower())
print(olympic_sport.capitalize())
print(olympic_sport.title())
print(str.title(olympic_sport), end='\n'*2)

print("Original book string:", book, end='\n')
print('title method using (book.title()')
print(book.title(), end='\n'*2)

print('title method using str.title(book)')
print(str.title(book), end='\n'*2)

print('string module with inherent capwords method')
print(string.capwords(book), end='\n'*2)     #string module using capwords

print('join method, capitalize method, split method')
print(' '.join(word.capitalize() for word in book.split()), end='\n'*2)

print('capitalize method with split method')
print([word.capitalize() for word in book.split()], end='\n'*2)

fruits = ['apple','grapes','orange']
print(f"Original list: {fruits}")
fruits = [i.title() for i in fruits]
print(f"'title method of a list: {fruits}", end='\n'*2)

print('join method, title method, split method')
print(' '.join([word.title() for word in book.split()]), end='\n'*2)

print('user defined fuction and re module - not working')
def convert_into_uppercase(a):     # not working correctly
    return a.group(1) + a.group(2).upper()
result = re.sub("(^|\s)(\S)", convert_into_uppercase, book)
print(result, ' - this function is not working correctly', end='\n'*2)

# accessing a file and changing the case of the first word, however, the change is not permanent
# how to permanently modify words in file?
print('capitalize each word in a file - not permanently within file')
file = open('Test_Hello_Case.txt', 'r')
for word in file: 
    output = word.title() 
    print(output)
