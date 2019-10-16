alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = str(input('Enter 26 character key: '))
function = str(input('Would you like to encrypt or decrypt? '))
usertext = str(input('Enter message: '))

def encrypt(string):
    result = ""
    for letter in string:
        if letter in alphabet:
            index = alphabet.index(letter)
            result = result + key[index]
    return result

def decrypt (string):
    result = ""
    for i in encrypt(string):
        if i in key:
            index = key.index(i)
            result = result + alphabet[index]
    return result

if function == 'encrypt':
    ciphertext = encrypt(usertext)
    print('Cipher text:', ciphertext)
elif function == 'decrypt':
    plaintext = decrypt(encrypt(usertext))
    print('Plain text:', plaintext)
