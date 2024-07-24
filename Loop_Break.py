# Loop Break
print('Without break in loop')
x_list = [1, 2, 3, 4]
for x in x_list:
    if x == 3:
        print('found item', x)
        # break
    else:
        print('Item not found')
    print(x)


print(end='\n')

print('With break in loop')
y_list = [1, 2, 3, 4]
for y in y_list:
    if y == 3:
        print('found item', y)
        break
    print(y)
else:
    print('Item not found')


