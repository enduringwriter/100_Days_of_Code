answers1 = ["A", "C", "B", "D"]
answers2 = ["A", "C", "", "D"]

# breaking out of a loop
for answer in answers1:
    if answer == "":
        print("Incomplete")
        break
    print(answer)
print("Loop is done\n")

for answer in answers2:
    if answer == "":
        print("Incomplete")
        break
    print(answer)
print("Loop is done\n")

# looping with continue
for answer in answers2:
    if answer=="":
        print("Incomplete")
        continue
    print(answer)
print("Loop is done")
