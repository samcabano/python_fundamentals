alphabet = ' abcdefghijklmnopqrstuvwxyz'
key = 'mwgp bdzxrylacsokjfhtnueivq'
plaintext = 'of shoes and ships and sealing wax of cabbages and kings'


def encrypt(string):
    result = ""
    for letter in string:
        if letter in alphabet:
            index = alphabet.index(letter)
            result = result + key[index]
    return result

print('Original text:', plaintext)

ciphertext = encrypt(plaintext)
print ('Encrypted text:', ciphertext)
