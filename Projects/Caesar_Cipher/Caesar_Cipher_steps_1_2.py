# Caesar Cipher
# decode and encode a message using a simple cipher that shifts the letters "n" amount

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# User input
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

# Decode issue for every full revolution of 26 
if shift%26 == 0:
    print("Please enter new shift that is not a multiple of 26. Multiples of 26 encodes to iself, for example, 'abc' shift 26 encodes to 'abc'")
    shift = int(input("Type the shift number: "))

def encrypt(plain_text, shift_amount, cipher_direction):
    cipher_text = ""
    for letter in plain_text:
        index_position = alphabet.index(letter)
        new_position = index_position + shift_amount
        if new_position > 25:
            x_factor = int(new_position/25)
            new_position = new_position - 26*x_factor
        cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")
    # return cipher_text

# test run
# encrypt("zab", 27)

def decrypt(cipher_text, shift_amount, cipher_direction):
    plain_text = ""
    for letter in cipher_text:
        index_position = alphabet.index(letter)
        new_position = index_position - shift_amount
        if new_position < -25:
            x_factor = int(new_position/25)
            new_position = new_position - 26*x_factor
        plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")

# test run
# decrypt("z", 27)

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift, cipher_direction=direction)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift, cipher_direction=direction)

# Alternate solution for index out of range error that occurs when shifting beyond "z"
# is doubling the alphabet. index() fuction searches for the first value it finds
# however, if the shift amount is greater than 26, this will not work
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     index_position = 0
#     new_position = 0
#     for letter in plain_text:
#         index_position = alphabet.index(letter)
#         new_position = index_position + shift_amount
#         cipher_text += alphabet[new_position]
#     print(f"The encoded text is {cipher_text}")
#     return cipher_text

# encrypt(plain_text=text, shift_amount=shift)