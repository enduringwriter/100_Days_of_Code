# Pizza Order

print("Welcome to Python Pizza Deliveries!")
bill = 0

# Size of Pizza
size = input("What size pizza do you want? S M L ")
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

# Add Pepporoni
add_pepporoni = input("Do you want pepporoni? Y N ")
if add_pepporoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Extra Cheese
extra_cheese = input("Do you want extra cheese? Y N " )
if extra_cheese == "Y":
    bill += 1

# Output Bill
print(f"Your final bill is ${bill}")