# Handling Errors - ZeroDivisionError and ValueError
# Try-Except blocks handle the exceptions and allows the code to continue running
# Without handling the Exception, the program will halt and show a Traceback

def divide_numbers_game():
    print("Divide two numbers game.")
    print("Enter 'q' to quit.")

    play_game = True

    while play_game:
        first_number = input("\nFirst number: ").lower()
        if first_number == 'q':
            break
        second_number = input("Second number: ").lower()
        if second_number == 'q':
            break

        try:
            answer = int(first_number) / int(second_number)
        except ZeroDivisionError:
            print("You can't divide by 0!")
        except ValueError:
            print("You must enter a number or 'q' to quit.")
        else:
            print(answer)


divide_numbers_game()
