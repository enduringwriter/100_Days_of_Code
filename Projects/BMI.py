# Calculate Body Mass Index (BMI), a measure of body fat based on height and weight
# BMI is based on metric units

# Input User Information
weight = float(input("enter your weight in kg: "))
height = float(input("enter your height in m: "))

# Calculation
bmi = round(weight / height ** 2)   # Cannot use int() because it truncates decimal instead of rounding
print(bmi)

# Condition and Output of Solution
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
