# Calculate Body Mass Index (BMI), a measure of body fat based on height and weight
# BMI is based on metric units, but an English conversion is provided

choice = input("Body Mass Index (BMI) Calculator. Type 'M' for Metric or 'E' for English").lower()

# one way of solving
if choice == "m":
    customer_weight = float(input("Enter your weight in kilograms: "))
    customer_height = float(input("Enter your height in meters: "))
    bmi = round(customer_weight/customer_height**2, 1)

else:
    customer_weight = float(input("Enter your weight in pounds: "))
    customer_height = float(input("Enter your height in inches: "))
    # 703 is the multiplication factor from metric to English
    bmi = round(703 * customer_weight / customer_height ** 2, 1)

if bmi < 18.5:
    bmi_status = "underweight"
elif bmi < 25:
    bmi_status = "normal weight"
elif bmi < 30:
    bmi_status = "overweight"
else:
    bmi_status = "obese"

print(f"Your BMI is {bmi}, you are {bmi_status}.")

# another way of solving
# if choice == "m":
#     unit_weight = "kilograms"
#     unit_height = "meters"
#     factor = 1
# else:
#     unit_weight = "pounds"
#     unit_height = "inches"
#     factor = 703  # conversion of English to metric, 1m = 39.37lbs and 1kg = 2.205inches
#
# customer_weight = float(input(f"Enter your weight in {unit_weight}: "))
# customer_height = float(input(f"Enter your height in {unit_height}: "))
#
# bmi = round(factor*customer_weight/customer_height**2, 1)
#
# if bmi < 18.5:
#     bmi_status = "underweight"
# elif bmi < 25:
#     bmi_status = "normal weight"
# elif bmi < 30:
#     bmi_status = "overweight"
# else:
#     bmi_status = "obese"
#
# print(f"Your BMI is {bmi}, you are {bmi_status}.")
