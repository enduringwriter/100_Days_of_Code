# using json.load()
# json stands for JavaScript Object Notation

import json

filename = "numbers.json"

with open(filename) as file:
    numbers = json.load(file)

print(numbers)
