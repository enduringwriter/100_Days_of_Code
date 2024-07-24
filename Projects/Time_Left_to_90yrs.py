# Time Left to Live, 90
# Learn f-String

# Input User Information
age = int(input("What is your current age? "))

# Calculation
years_remaining = 90-age
days_remaining = int(years_remaining*365)
weeks_remaining = int(years_remaining*52)
months_remaining = int(years_remaining*12)

# Output Solution
time_left = f"You have {days_remaining} days, {weeks_remaining}, and {months_remaining} left"
print(time_left)

# Output of Alternative Solution
# print("You have", days, "days,", weeks, "weeks, and", months, "months left")
