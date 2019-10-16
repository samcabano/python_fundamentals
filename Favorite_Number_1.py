favnum = input('Enter your favorite number: ')

favnumFile = open('favnum.txt', 'w')
favnumFile.write(favnum)
favnumFile.close()