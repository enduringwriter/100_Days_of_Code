# Handling Errors - FileNotFoundError

filename = 'howdy.txt'


def open_files():
    with open(filename) as file:
        contents = file.read()
    return contents


try:
    open_files()
except FileNotFoundError:
    msg = f"The file {filename} does not exist."
    print(msg)
