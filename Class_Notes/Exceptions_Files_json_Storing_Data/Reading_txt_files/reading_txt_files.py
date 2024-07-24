# learn to open and read a .txt file

# ---- .txt file located in same directory with the .py file

filename = "txt_files_same_dir.txt"

# reading the entire file - .read()
print("\n---- Reading the entire file - read():")
with open(filename, "rt") as file:  # default is set to "rt" where "r" is read mode and "t" is text mode
    content = file.read()
    print(content)

# reading line by line - looping over the lines
print("\n---- Reading line by line - for loop:")
with open(filename) as file:
    for line in file:
        print(line.rstrip())

# when using "with", the file accessed by open() is only available inside the "with" block
# "with" closes the file once it is no longer needed
# to retain access to the file's contents outside the "with" block, use .readlines()

# making a List of Lines from a File - .readlines()
print("\n---- Making a List of Lines from a File - .readlines() and for loop over the lines:")
with open(filename) as file:
    lines = file.readlines()  # .readlines() method takes each line from the file and stores it in a list

for line in lines:
    print(line.rstrip())

# # alternative method to read file, but it doesn't use 'with' to close the file
# print("---- Reading the entire file:")
# file1 = open("txt_files_same_dir.txt")
# print(file1.read())

# ---- .txt file located in a different directory than the .py file

# relative path, the directory where the .txt file is located must be in the directory were .py file is located
print("\n---- Reading the entire file from a directory that is within the .py dir - read() and relative path:")
with open('sub_dir/txt_files/txt_files_diff_dir.txt') as file:
    content = file.read()
    print(content)

# absolute path, the directory where the .txt file is located can be anywhere
# Mac default OS file system is case-insensitive
print("\n---- Reading the entire file from a different directory - read() and absolute path:")
file_path = '/users/keithstateson/dir_files_py_pract/txt_files_any_dir.txt'
# file_path = '~/dir_files_py_pract/txt_files_any_dir.txt'  # "~/" represents the user's home directory

with open(file_path) as file:
    content = file.read()
    print(content)

# ---- Working with a File's Content using readlines()
# ---- readline() only reads the first line in the file, whereas readlines() reads all lines in the file
print("\n---- Combining lines into one string:")
with open(filename) as file:
    lines = file.readlines()  # .readlines() method takes each line from the file and stores it in a list

single_string = ""
for line in lines:
    single_string += line.rstrip() + ", "

print(single_string[49:69], "and", single_string[121:146])
print(len(single_string), "characters in the string.")
