alphabet = 'abcdefghijklmnopqrstuvwxyz '
key = 'mwgp bdzxrylacsokjfhtnueivq'
ciphertext = 'hz qftcqumfqfzxcxcdqscqhz qf mqfzxcxcdquxhzqmllqzxfqaxdzh'

def encrypt(string):
    result = ""
    for letter in string:
        if letter in alphabet:
            index = alphabet.index(letter)
            result = result + key[index]
    return result

def decrypt (string):
    result = ""
    # for i in encrypt(string):
    for i in string:
        if i in key:
            index = key.index(i)
            result = result + alphabet[index]
    return result

print('Cipher text:', ciphertext)

plaintext = decrypt(ciphertext)
print('Plain text:', plaintext)
