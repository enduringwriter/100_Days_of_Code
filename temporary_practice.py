# use numpy.array to modify all variables within an array

import numpy as np

x = ()
y = ()

x = np.array([1, 2, 3])
print(f'original numpy array: {x}')
print(type(x))

x = x*2
print(f'New arrray, x = x * 2: {x}')

y = x + 10
print(f'New array, y = x + 10: {y}')
print(type(y))

w = x+y
print(f'New array, w = x + y: {w}')
print(type(w))

z = np.concatenate((x, y))
print(f'np.concatentate to join 2 or more arrays, z = x + y: {z}')
print(type(z))

print('convert numpy arrays to a list')
a = list(x)
b = list(y)
c = list(w)
d = list(z)
print(a+b, '\t', 'list x + list y')
print(a,b, '\t', 'list x, list y')
print(c, '\t'*2, 'list w')
print(d, '\t', 'list z')
