# pw.py - An insecure password manager.

import random
import pyperclip
import sys

# global variables for security
encrypted_master = 'XMxrmFvdMxxlEF^' # Store the master password encrypted (decrypted = 'master password')
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456890!@#$%^&*() '
key = 'S0L9182W7D3C6B4A5)!(@U*#N&M$%^mYwOVgp XbEdzFxrGylaHTcIsPoJkjfhtnRKuQeiZvq'

# main menu
def get_menu_option():
    print()
    option = input('Menu: A)dd Accounts, F)ind Password, P)rint Accounts, U)pdate Password, S)how Encrypted Passwords, Q)uit: ').strip()
    return option.upper()

# password menu
def get_pwd_option():
    print()
    option = input('Menu: G)enerate password, E)nter your own password: ').strip()
    if option.upper() not in ('G', 'E'): # error message if invalid input, restarts loop
        print('Invalid response.  Please enter G or E.')
        return get_pwd_option()
    else:
        return option.upper()    

# displays account names
def show_key(keys):
    for i in keys.keys():
        print (i)

# displays encrypted passwords
# included ability to show that passwords are stored as encrypted values
def show_pwd(values):
    for i in values.values():
        print (i)     

# requires master password to decrypt passwords
# quits program if password incorrect after 3 tries
def login():   
    for i in range(1, 4):
        master_pwd = encrypt(input('Enter the master password: ')) 
        if master_pwd == encrypted_master:
            return
        else:
            if i < 3:
                print('Invalid master password. ', i, 'of 3 tries used.')
            elif i == 3:
                print('Maximum tries reached. Goodbye!')
                quit()       

# encrypts passwords
def encrypt(string):
    result = ""
    for letter in string:
        if letter in alphabet:
            index = alphabet.index(letter)
            result = result + key[index]
    return result

# decrypts passwords copied to clipboard
def decrypt (string):
    result = ""
    for i in string:
        if i in key:
            index = key.index(i)
            result = result + alphabet[index]
    return result

# main program: executes menu and functions
def main():
    # Decrypted password key:
    #           gmail : Google123@
    #           facebook : fbPwd!24
    #           twitter : Tweets#3
    #           instagram : 4daGram
    passwords = {'gmail' : '2EEw mcIst',
              'facebook' : '0n4gpSGO',
              'twitter' : 'zg**@3XK',
              'instagram' : 'Opxutxe'}

    # calls menu function
    option = get_menu_option()
    while option != 'Q': # quits program
        if option == 'A': # adds new account to dictionary
            key_to_add = input('Enter account to add: ')
            print('New account added.')
            pw = get_pwd_option() # displays password menu
            if pw == 'G': # generates XKCD password
                # lists of random nouns, verbs, and adjectives for generator to choose from
                nouns = ['tissue', 'processor', 'headquarters', 'favorite', 'cure', 'ideology', 'funeral', 'engine', 'isolation', 'perception', 'hat', 'mountain', 'session', 'case', 'legislature', 'consent', 'spread', 'shot', 'direction', 'data', 'tragedy', 'illness', 'serving', 'mess', 'resistance', 'basis', 'kitchen', 'mine', 'temple', 'mass', 'dot', 'final', 'chair', 'picture', 'wish', 'transfer', 'profession', 'suggestion', 'purse', 'rabbit', 'disaster', 'evil', 'shorts', 'tip', 'patrol', 'fragment', 'assignment', 'view', 'bottle', 'acquisition', 'origin', 'lesson', 'Bible', 'act', 'constitution', 'standard', 'status', 'burden', 'language', 'voice', 'border', 'statement', 'personnel', 'shape', 'computer', 'quality', 'colony', 'traveler', 'merit', 'puzzle', 'poll', 'wind', 'shelter', 'limit', 'talent']
                verbs = ['represent', 'warm', 'whisper', 'consider', 'rub', 'march', 'claim', 'fill', 'present', 'complain', 'offer', 'provoke', 'yield', 'shock', 'purchase', 'seek', 'operate', 'persist', 'inspire', 'conclude', 'transform', 'add', 'boast', 'gather', 'manage', 'escape', 'handle', 'transfer', 'tune', 'born', 'decrease', 'impose', 'adopt', 'suppose', 'sell', 'disappear', 'join', 'rock', 'appreciate', 'express', 'finish', 'modify', 'keep', 'invest', 'weaken', 'speed', 'discuss', 'facilitate', 'question', 'date', 'coordinate', 'repeat', 'relate', 'advise', 'arrest', 'appeal', 'clean', 'disagree', 'guard', 'gaze', 'spend', 'owe', 'wait', 'unfold', 'back', 'waste', 'delay', 'store', 'balance', 'compete', 'bake', 'employ', 'dip', 'frown', 'insert']
                adjs = ['busy', 'closer', 'national', 'pale', 'encouraging', 'historical', 'extreme', 'cruel', 'expensive', 'comfortable', 'steady', 'necessary', 'isolated', 'deep', 'bad', 'free', 'voluntary', 'informal', 'loud', 'key', 'extra', 'wise', 'improved', 'mad', 'willing', 'actual', 'OK', 'gray', 'little', 'religious', 'municipal', 'just', 'psychological', 'essential', 'perfect', 'intense', 'blue', 'following', 'Asian', 'shared', 'rare', 'developmental', 'uncomfortable', 'interesting', 'environmental', 'amazing', 'unhappy', 'horrible', 'philosophical', 'American']

                # random function chooses 2 words from nouns list, 1 word from adj, 1 word from verbs
                value_to_add = encrypt(random.choice(nouns) + random.choice(verbs) + random.choice(adjs) + random.choice(nouns))
            elif pw == 'E': # enter your own password    
                value_to_add = encrypt(input('Enter password for %s account: ' % key_to_add))
            print('New password generated for %s!' % key_to_add)                
            passwords[key_to_add] = value_to_add # assigns password to new account
    
        elif option == 'F': # finds account
            login() # requires master password for decryption
            item_to_find = input('Enter an account to find: ')
            if item_to_find in passwords: # copies password to clipboard
                pyperclip.copy(decrypt(passwords[item_to_find]))
                print('Password for %s copied to clipboard.' % item_to_find)
            else:
                print('There is no account named ' + item_to_find)
            
        elif option == 'U': # updates existing password
            login() # requires master password to change existing password
            item_to_find = input('Enter an account to update: ')
            if item_to_find in passwords: 
                value_to_add = encrypt(input('Enter new password for %s account: ' % item_to_find))
                print('Password for %s updated.' % item_to_find)
            else:
                print('There is no account named ' + item_to_find)
            passwords[item_to_find] = value_to_add

        elif option == 'P': # prints list of accounts
            show_key(passwords)

        elif option == 'S': # prints list of encrypted passwords
            show_pwd(passwords)    
           
        else:
            print('Invalid option.')

        option = get_menu_option()

# executes program
main()
