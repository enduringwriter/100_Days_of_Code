# Calculate Body Mass Index (BMI), a measure of body fat based on height and weight
# BMI is based on metric units, but an English conversion is provided

calculate_bmi = True
unit_weight = 0
unit_height = 0
unit_conversion = 1

def bmi_calculator(conversion_factor, weight, height):
    """
    Given a patient's weight and height, determine the patient's BMI and weight status
    :param conversion_factor: 1 for metric, 703 for English
    :param weight: 150 pounds
    :param height: 70 inches
    :return: BMI = 21.5, weight_status = "normal weight"
    """
    bmi = round(conversion_factor*weight/height**2, 1)

    if bmi < 18.5:
        weight_status = "underweight"
    elif bmi < 25:
        weight_status = "normal weight"
    elif bmi < 30:
        weight_status = "overweight"
    else:
        weight_status = "obese"
    return print(f"Your BMI is {bmi}, you are {weight_status}.")


print("Welcome to Body Mass Index (BMI) Calculator")
while calculate_bmi:
    choice = input("Type 'M' for Metric or 'E' for English, or 'q' to quit: ").lower()
    if choice == "q":
        calculate_bmi = False
        print("Goodbye")
        break
    elif choice == "m":
        unit_weight = "kilograms"
        unit_height = "meters"
        unit_conversion = 1
    elif choice == "e":
        unit_weight = "pounds"
        unit_height = "inches"
        unit_conversion = 703  # conversion of English to metric, 1m = 39.37lbs and 1kg = 2.205inches
    else:
        print("Enter 'm', 'e', or 'q'")

    patient_weight = float(input(f"Enter your weight in {unit_weight}: "))
    patient_height = float(input(f"Enter your height in {unit_height}: "))
    bmi_calculator(conversion_factor=unit_conversion, weight=patient_weight, height=patient_height)
