# Caesar Cipher
# decode and encode a message using a simple cipher that shifts the letters "n" amount

from art import logo

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Cipher code
def caeser_cipher(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for character in start_text:
        if character in alphabet:    
            index_position = alphabet.index(character)
            new_position = index_position + shift_amount
            # if new_position > 25 or new_position < -25:
            #     x_factor = int(new_position/25)
            #     new_position = new_position - 26*x_factor
            end_text += alphabet[new_position]
        else:
            end_text += character   # alternate method is to add space and special characters to the alphabet string.
    print(f"The {cipher_direction}d text is {end_text}")
    # return

print(logo)

end_program = False
while not end_program:
    # User input
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

  # Issue warning that multiples of 26 encode to iself, for example, 'abc' shift 26 encodes to 'abc'.
    while shift%26 == 0:
        print("Warning. Please enter new shift that is not a multiple of 26.")
        shift = int(input("Reenter the shift number: "))
        continue

    # simplified version, but would have to doubl the alphabet to cover shift past "z"
    shift = shift%26

    caeser_cipher(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    run_cipher_again = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")
    if run_cipher_again == "no":
        end_program = True
        print("Goodbye")
