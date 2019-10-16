def encrypt(original, shift):
	output = []
	crypt = []
	
	uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	for letter in original:
		if letter in uppercase:
			index = uppercase.index(letter)
			newIndex = (index + shift) % 26
			crypt.append(newIndex)
			result = uppercase[newIndex]
			output.append(result)
		elif letter in lowercase:
			index = lowercase.index(letter)
			newIndex = (index + shift) % 26
			crypt.append(newIndex)
			result = lowercase[newIndex]
			output.append(result)
	return''.join (output)

phrase = 'thequickbrownfoxjumpsoverthelazydog'
shift = 13

print('Original text:', phrase)
print('Shift:', 13)
code = encrypt(phrase, shift)
print('Ciphered text:', code)
