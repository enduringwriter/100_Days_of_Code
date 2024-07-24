# Splitting a String - re.split vs native .split

import re

x = '/usr/home:lumberjack'
print(f"Original list is: {x}")

#### re.split()
print('using re.split')
x_list = re.split('[/:]', x)
print(x_list)

#### native .split()
print('using native python .split twice and index assignment')
y_list = x.split('/')
print(y_list)
z_list = y_list[2].split(':')
print(z_list)
y_list[2] = ''  # clear index[2] in y_list b/c it has the old value ':'
yz = y_list + z_list
print(yz)
