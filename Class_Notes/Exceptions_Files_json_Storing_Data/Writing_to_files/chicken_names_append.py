# append to a file

filename = 'chicken_names.txt'

with open(filename, 'a') as file:
    file.write("KFC\n")
    file.write("Church's\n")
    file.write("Popeyes\n")
    file.write("Raising Cane's\n")
    file.write("Bushes\n")
