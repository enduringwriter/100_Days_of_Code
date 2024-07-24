# Searching and Getting Substrings

import re

str = "i say To you: it's not too DIFFICULT to lEArn TONS of 10a PythoN if doing projects"

#### Getting Index
# re re.search(r'...', str)
# .start() and .end() of re module outputs start index and end index
find_to = re.search(r'to', str)
start_to = find_to.start()
end_to = find_to.end()
print(f"Class type of variable 'find_to': {type(find_to)}")
print(f"Start index using re.search(r'to', str) and .start(): {start_to}")
print(f"End index using re.search(r'to', str) and .end(): {end_to}") # up to but not including

# .find outputs index of first letter of searched substring
print(f"Index of 'to' using .find('to'): {str.find('to')}")

#### Getting Specified Substring
# .group() of re module converts the index value into a string
var_to = find_to.group()
print(f"Class type of variable 'var_to': {type(var_to)}")
print(f"Substring using .group(): {var_to}")

# using index range to get substring 
print(f"Substring using index range: {str[start_to:end_to]}")

#### Getting All Specified Substrings
# re.findall(r'...', str)
find_all_to = re.findall(r'[Tt][Oo]', str)
print(f"Class type of variable 'find_all_to': {type(find_all_to)}")
print(f"All substrings with 'to', case insensitive: {find_all_to}")
print(f"index [0] in find_all_to: {find_all_to[0]}")

# re.findall(r'...', str) and use ^ to not search for specific substrings
find_all_py = re.findall(r'[Pp][^Rr, ' ']', str)  # search for words that begin with P or p, but omit words if the second letter begins with R or r or a space
print(f"All substrings with 'py', case insensitive: {find_all_py}")

#### Get Substring Within a String
# re.match('', str)
print(f"Original string: {str}")
findsubstring1 = re.match('i say To you: *(.*)if', str)
print(f"Class type of findsubstring1: {type(findsubstring1)}")
substring1 = findsubstring1.group(1)  # must include '1' in .group(1)
print(f"Class type of substring1: {type(substring1)}")
print(f"substring1 is: {substring1}")
