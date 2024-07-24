# numpy.array to modify all variables within a sequence

import numpy as np

x = ()
y = ()

x = np.array([1, 2, 3])
print(f'original numpy array: {x}')
# print(type(x))

x = x*2
print(f'New arrray, x = x * 2: {x}')

y = x + 10
print(f'New array, y = x + 10: {y}')
# print(type(y))

w = x+y
print(f'New array, w = x + y: {w}', end="\n"*2)
# print(type(w))

z = np.concatenate((x, y))
print(f'np.concatentate to join 2 or more arrays, z = x + y: {z}', end="\n"*2)
# print(type(z))

print('convert all 4 numpy arrays to a list')
a = list(x)
b = list(y)
c = list(w)
d = list(z)
print(a+b, '\t', 'list x + list y')
print(a,b, '\t', 'list x, list y')
print(c, '\t'*2, 'list w')
print(d, '\t', 'list z')

#
# compare numpy.array vs for loop and .append to modify all variables within a sequence
import numpy as np


seq = [1, 2, 3]
print(f"Original list: {seq}")

# numpy.array method
seq_array = np.array(seq)
print(f"Method 1, use numpy.array: {seq_array + 10}")

# for loop and .append method
seq_mod = []
for x in seq:
    seq_mod.append(x + 10)
    # x += 10
    # seq_mod.append(x)
print(f"Method 2, use for loop and .append: {seq_mod}")
