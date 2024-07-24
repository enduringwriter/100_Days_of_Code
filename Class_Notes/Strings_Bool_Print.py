# Strings Len Strip Print
print('Strings Len Strip Print')
x = 'Hello'
y = 'Earthlings'
z = ''
print('x = ', x, '\n', '\by = ', y, '\n', 'z = ', z, end='\n'*2)  # \b means backspace by 1 place

# Len function - length of a string
print('Len Function')
print('length x = ', len(x), 'length y = ', len(y))
print('total length = ', len(x+y))
print("len of print(len('A\\nB\\tC')) outputs: ", len('A\nB\tC'),
      ' b/c special characters count as 1 character', end='\n'*2)

# Strip Strings
print('Strip Strings')
state = '  Texas  '
print('USA', state.lstrip(), 'USA')
print('USA', state.rstrip(), 'USA')
print('USA', state.strip(), 'USA')
print('USA' + state.strip() + 'USA', end='\n'*2)

# Boolean Conversion
print(
    'Boolean Conversion',
    bool(1),
    bool(0),
    bool('Hello'),
    bool(['Hello', 'Earthlings', '']),
    bool(''),
    sep='\n', end='\n'*2)

# Boolean Strings
x = 'Hello'
y = 'Earthlings'
z = ''
print('Boolean Strings')
print([bool(x),bool(y),bool(z)])
print(bool(x), bool(y),bool(z), end='\n'*2)

# Boolean String Counting
print('Counting Strings using Boolean')
print('Total True using count: ', [bool(x),bool(y),bool(z)].count(True))
print('Total False using count: ', [bool(x),bool(y),bool(z)].count(False))
print('Total Trues using sum: ', sum([bool(x),bool(y),bool(z)]))
w = [bool(x),bool(y),bool(z)]
print('Average Truth (Trues) using sum and count: ', sum(w)/(w.count(True)+w.count(False)))

# Class Types
print("list: ", type([{}]))  # [{}]
print("dictionary: ", type({'a': []}))  # {'a': []}
