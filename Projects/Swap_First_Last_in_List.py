# Swap the first and last element in a list
 
# Swap function with x being the list passed into it
def swap_f_and_l(x):
    size = len(x)
    # test code
    # print(size)
     
    # Swapping first and last item in list "x"
    temp = x[0]
    x[0] = x[size - 1]
    x[size - 1] = temp
     
    return x

numbers = [12, 3, 7, 24]

print(f"\nOriginal list of numbers: {numbers}")
print(f"New list with first and last swapped: {swap_f_and_l(x = numbers)}\n")