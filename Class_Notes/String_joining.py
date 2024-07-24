arr = ['sunday', 'monday', 'tuesday', 'wednesday']

# map function requires 2 parameters, one of them must be a function

# using map and .join
x = ' '.join(map(str, arr))
print(x)

b = ' '.join(map(str, range(1, 5)))
print(b)

# using map and a function
y = ['Hello', "world"]
yy = list(map(str.upper, y))
print(yy)

# using for loop
string_of_items = ""
for item in arr:
    string_of_items += item + ' '
print(string_of_items)

# using asterisk
print(*arr)
