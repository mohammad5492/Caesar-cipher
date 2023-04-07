
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input('Enter "encode" or "decrypt": ')
text = input('Enter your message: ').lower()
shift = int(input('Enter your shift number: '))

def encrypt(plain_text, shift_number):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_number
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f'The {direction}ed text is: {cipher_text}')



def decrypt(cipher_text,shift_amount):
    plain_text = " "
    for letter in cipher_text:
        positon = alphabet.index(letter)
        new_positon = positon - shift_amount
        plain_text += alphabet[new_positon]
    print(f"The decrypted text is: {plain_text}")


if direction == "encode":
    encrypt(plain_text=text, shift_number=shift)
elif direction == "decrypt":
    decrypt(cipher_text=text, shift_amount=shift)
