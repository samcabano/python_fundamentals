# Fundamentals of Programming in Python
Attached are examples of small projects written in Python, all of which demonstrating basic Python fundamentals. Contents of the portfolio are organized by the primary fundamental explored, and link to the raw code of each project. Each of the following pieces were created to practice and learn a focused concept of Python.

## Contents

- ### Introduction

     - [Hello Turtle](https://github.com/samcabano/python_fundamentals/blob/master/Module%201%20-%20Introduction/Hello_Turtle.py): Simple program using turtle graphics system.

- ### Flow Control

     - [How Many Trees?](https://github.com/samcabano/python_fundamentals/blob/master/Module%202%20-%20Flow%20Control/How_Many_Trees.py): Calculates the number of trees in Sacramento using flow control.
    
- ### Conditionals and Lists

     - [Password Generator](https://github.com/samcabano/python_fundamentals/blob/master/Module%203%20-%20%20Conditionals%20and%20Lists/Password_Generator.py): Generates two random passwords utilizing lists, flow control, and conditionals.
     - [Rock, Paper, Scissors](https://github.com/samcabano/python_fundamentals/blob/master/Module%203%20-%20%20Conditionals%20and%20Lists/Rock_Paper_Scissor.py): Simple game that utilizes conditionals to determine the winner. 

- ### More Lists, and Introduction to Functions

    - [Comma Code](https://github.com/samcabano/python_fundamentals/blob/master/Module%204%20-%20Introduction%20to%20Functions/Comma_Code.py): Function that turns list values into a formatted string.
    - [Collatz Sequence](https://github.com/samcabano/python_fundamentals/blob/master/Module%204%20-%20Introduction%20to%20Functions/Collatz_Sequence.py): Function that requests the input of an integer, which is then evaluated and returned to 1.
    - [Character Picture Grid](https://github.com/samcabano/python_fundamentals/blob/master/Module%204%20-%20Introduction%20to%20Functions/Character_Pic_Grid.py): Function that returns a picture drawn by lists of text characters.

- ### Functions and Dictionaries

    - [Substitution Cipher](https://github.com/samcabano/python_fundamentals/blob/master/Module%205%20-%20Functions%20and%20Dictionaries/Substitution_Cipher.py): Decrypts a secret message bkftazdaowe to pythonrocks utilizing dictionaries and conditionals.
    - [Caesar Cipher](https://github.com/samcabano/python_fundamentals/blob/master/Module%205%20-%20Functions%20and%20Dictionaries/Ceasar_Cipher.py): Encrypts plain text by shifting the alphabet 13 letters.
    - [Caesar Cipher Rotation Possibilities](https://github.com/samcabano/python_fundamentals/blob/master/Module%205%20-%20Functions%20and%20Dictionaries/Ceasar_Cypher_Rotations.py): Decrypts ciphered text by printing all 25 possible rotations.  
    - [Scrambled Key Decryption](https://github.com/samcabano/python_fundamentals/blob/master/Module%205%20-%20Functions%20and%20Dictionaries/Scrambled_Key_Decryption.py): Decrypts ciphered text against a key of scrambled alphabet.
    - [Scrambled Key Encryption](https://github.com/samcabano/python_fundamentals/blob/master/Module%205%20-%20Functions%20and%20Dictionaries/Scrambled_Key_Encryption.py): Encrypts plain text by using a key of scrambled alphabet.
    - [Encryption and Decryption](https://github.com/samcabano/python_fundamentals/blob/master/Module%205%20-%20Functions%20and%20Dictionaries/Encryption_Decryption.py): Prompts the user to enter a key, gives the user the option to encrypt plain text or decrypt a coded message.

- ### Strings and Exception Handling

    - [Password Manager](https://github.com/samcabano/python_fundamentals/blob/master/Module%206%20-%20Strings%20and%20Exception%20Handling/Password_Manager.py): Utilizes multiple functions, dictionaries, lists, strings, and conditionals to store account passwords, encrypt and generate passwords, update passwords, and copy passwords to clipboard. 
    
- ### Reading and Writing Files

    - [Store Your Favorite Number](https://github.com/samcabano/python_fundamentals/blob/master/Module%207%20-%20Reading%20and%20Writing%20Files/Favorite_Number_1.py): Propts user to enter favorite number, storing it in a file.
    - [Display Your Favorite Number](https://github.com/samcabano/python_fundamentals/blob/master/Module%207%20-%20Reading%20and%20Writing%20Files/Favorite_Number_2.py): Reads the file and prints the user's favorite number.

## Summary

The most comprehensive and challenging project I completed in Unit 1 was the creation of a Password Manager, which incorporates each major concept of the course thusfar. I am proud of the code I produced for this assignment, as I feel it displays the most complex functions of anything we have practiced in Unit 1. This project taught me the importance of having organized code with detailed comments, as it required the definition of several variables and functions. To complete this project, I drew a flowchart indicating each desired function of the program, then implemented a function one by one. During the process, I learned it is important to run your code between each change, otherwise it is difficult to find the source of a coding error.

On the other hand, I would remove cipher code listed under "Functions and Dictionaries", as it is redundant of the encryption and decryption code used in later projects. While writing code for various encryption and decryption exercises, I found it challenging to decide between the use of dictionaries, lists, or strings to assign encryption key values. By practicing with each, I found the use of strings for this task allowed for more effective and dynamic code.

#### For example:

A dictionary was used in my Substitution Cipher:
```python
key = {"a" : "o", "b" : "p", "c" : "q", "d" : "r", "e" : "s", "f" : "t", "g" : "u", "h" : "v", "i" : "w", "j" : "x", "k" : "y", "l" : "z", "m" : "a", "n" : "b", "o" : "c", "p" : "d", "q" : "e", "r" : "f", "s" : "g", "t" : "h", "u" : "i", "v" : "j", "w" : "k", "x" : "l", "y" : "m", "z" : "n"}

def decode(str, key):
    result = ""
    for i in str:
        result = result + key[i]
    return result
```
A list was used in my Caesar Cipher to shift the index of a phrase by a specified number:
```python
def encrypt(original, shift):
	output = []
	crypt = []
	
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	for letter in original.lower():
		index = alphabet.index(letter)
		newIndex = (index + shift) % 26
		crypt.append(newIndex)
		result = alphabet[newIndex]
		output.append(result)
	return''.join (output)

phrase = 'THEquickbrownfoxjumpsoverthelAZydog'
shift = 13

print('Original text:', phrase)
print('Shift:', 13)
code = encrypt(phrase, shift)
print('Ciphered text:', code)
```
Strings were used in my Scrambled Key projects to compare corresponding index values between the alphabet and a scrambled key:
```python
alphabet = ' abcdefghijklmnopqrstuvwxyz'
key = 'mwgp bdzxrylacsokjfhtnueivq'

def encrypt(string):
    result = ""
    for letter in string:
        if letter in alphabet:
            index = alphabet.index(letter)
            result = result + key[index]
    return result
```
```
• What makes your strongest piece different from your weakest piece?
• What goals did you set for yourself? How well did you accomplish them?
• Why did you select this piece of work?
• What was particularly important to you during the process of creating this work?
• How does this relate to what you have learned before?
• Which piece would you most like to improve? Why?
• What is the one thing you would like someone to notice about your portfolio? Why?
• Do you feel that this collection of work really reflects your abilities and what you have achieved so far this year? Why or why not?
```

<p align="center">
  <a href="https://samcabano.github.io/cabano-profile/">Return to ABOUT ME</a>
</p>

