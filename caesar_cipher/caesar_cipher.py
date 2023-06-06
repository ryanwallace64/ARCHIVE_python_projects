alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
end_game = False

# Cipher code to shift letters by desired amount and then print output. Works for both plain and cipher text.
def caesar(start_text, shift_amount, cipher_direction):
    output = ""
    # Shift left (negative) if decoding, otherwise shift right
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            while new_position > 25:
                new_position -= 26
            while new_position < 0:
                new_position += 26
            output += alphabet[new_position]
        else:
            output += letter
    print(f"The {cipher_direction}d text is {output}.")

# Title art
from art import logo
print(logo)

# Continue playing until user enters no
while end_game == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    restart = input("Would you like to go again? Type 'yes' or 'no' ")
    if restart == "no":
        end_game = True