# Determine if patron is meets rollercoaster requirements, and if so, would like a picture?

# Input User Information
print("Welcome to the rollercoaster!")
height = int(input("What is your height in inches? "))

# Condition and Output of Solution
bill = 0

if height >= 48:
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    take_photo = input("Do you want a photo taken for $3? Y or N. ")
    if take_photo == "Y":
        bill += 3
        print(f"Your final bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride the rollercoaster.")
