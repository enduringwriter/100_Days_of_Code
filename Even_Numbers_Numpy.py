# Even numbers, using numpy array

import numpy as np

print('Even numbers, using numpy array', end='\n'*2)


def even_numbers_np_array(a, b):
    even_seq = np.array(range(a, b, 2))
    return even_seq


print(even_numbers_np_array(4, 15))
