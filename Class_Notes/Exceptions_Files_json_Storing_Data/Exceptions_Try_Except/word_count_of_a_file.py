# count the number of words in a file


def count_words(name_of_file):
    """Count the number of words in a file."""
    try:
        with open(name_of_file) as file:
            content = file.read()
    except FileNotFoundError:
        # msg = f"The file {name_of_file} does not exist."
        # print(msg)
        pass
    else:
        words = content.split()
        number_of_words = len(words)
        print(f"The file {filename} has about {number_of_words:,} words.")


filenames = ["seven_with_one_blow.txt",
             "The_Adventures_of_Sherlock_Holmes.txt",
             "Grimms'_Fairy_Tales.txt"]
for filename in filenames:
    count_words(filename)
