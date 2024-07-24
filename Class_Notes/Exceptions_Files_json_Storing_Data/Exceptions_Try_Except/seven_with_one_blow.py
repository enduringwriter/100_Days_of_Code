filename = "seven_with_one_blow.txt"

try:
    with open(filename) as file:
        content = file.read()
except FileNotFoundError:
    msg = f"The file {filename} does not exist."
    print(msg)
else:
    words = content.split()
    number_of_words = len(words)
    print(f"The file {filename} has about {number_of_words} words.")

# # adding count function
# filename = "seven_with_one_blow.txt"
#
#
# def count_words(name_of_file, content_of_file):
#     words = content_of_file.split()
#     number_of_words = len(words)
#     print(f"The file {name_of_file} has {number_of_words:,} words.")
#
#
# try:
#     with open(filename) as file:
#         content = file.read()
# except FileNotFoundError:
#     msg = f"The file {filename} does not exist."
#     print(msg)
# else:
#     count_words(filename, content)
