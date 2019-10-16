favnumFile = open('favnum.txt')

display = favnumFile.read()
favnumFile.close()

print('Your favorite number is', display)
