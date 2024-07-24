import re

str_test = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str_test)

# If-statement after search() tests if it succeeded
if match:
    print('found', match.group())  # 'found word:cat'
else:
    print('did not find')
