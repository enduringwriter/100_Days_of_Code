# Create a map where the user enters a 2-digit number corresponding to an X on the map
# Learn about nested lists and replacing a value

# Map creation
# column 1 2 3 by row 1 2 3     therefore subtract 1 from user column and row input
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

# Input 2-digit number
position = input("Where do you want to put the treasure? ")

# Convert single string to a list to separate the characters
position_split_string = list(position)

# Convert each sting in the list to an integer
# Ten's digit is the column and the one's digit is the row
column = int(position_split_string[0])
row = int(position_split_string[1])
map[row-1][column-1] = "X"

# Calculation simplified
#row = int(position[1])
# column = int(position[0])
# map[row-1][column-1] = "X"

# Output Solution
print(f"{row1}\n{row2}\n{row3}")