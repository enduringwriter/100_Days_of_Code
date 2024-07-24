from name_function import get_formatted_name

print("Enter 'q' at anytime to quit.")
while True:
    first = input("Enter first name: ")
    if first == 'q':
        break
    last = input("Enter last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}")
