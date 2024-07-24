# Format Names to title format
# if input is keith or KEITH, the output is: Keith
# if the entry is blank, notify the user

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "One or more inputs is blank."
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))
