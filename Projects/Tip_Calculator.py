# Tip Calculator for one or more persons

# Input User Information
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? "))
total_people = int(input("How many people to split the bill? "))

# Calculation
tip_amount = tip/100    #convert tip entry to tip percent
total_bill_and_tip = total_bill + total_bill*tip_amount
ppp = total_bill_and_tip/total_people    # ppp = percentage per person

# Output Solution
print(f"Each person should pay: ${ppp:.2f}")

# Output of Alternative Solution
# ppp_two_decimals = "{:.2f}".format(ppp)
# print(f"Each person should pay: ${ppp_two_decimals}")
