"write to a file"
filename = 'bread.txt'

with open(filename, 'w') as file:
    file.write("Sourdough Boule from France or San Francisco\n")
    file.write("Salt Rising Bread from Colorado\n")
    file.write("Tortillas from Texas\n")
    file.write("French Bistro Roll from France\n")
    file.write("Rum Raisin Rolls from Amsterdam\n")
