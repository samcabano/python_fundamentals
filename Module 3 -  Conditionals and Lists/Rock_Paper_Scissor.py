import random 

print ("Rock, paper, scissors, shoot!")
player1 = input('Player 1 - Enter your choice: ')   # prompts user input of rock, paper or scissors

# For 2 player games, while loop to hide player 1's response, then requests response from player 2:
# n = 1
# while n < 50:
    # print ('\n')
    # n = n + 1
# player2 = input("Player 2 - Enter your choice: ")

rando = random.randint (0,2)                        # chooses rock, paper, or scissors by random
options = ['rock', 'paper', 'scissors']
player2 = options[rando]              

# Player 1 chooses rock
if (player1 == "rock" and player2 == "scissors"):   # rock beats scissors
    print("Player 2 chose:", player2)
    print("You win!!")
elif (player1 == "rock" and player2 == "paper"):    # paper beats rock
    print("Player 2 chose:", player2)
    print("Player 2 wins!!")
elif (player1 == "rock" and player2 == "rock"):     # tie
    print("Player 2 chose:", player2)
    print("Tie!!")
    
# Player 1 chooses paper
elif (player1 == "paper" and player2 == "scissors"):
    print("Player 2 chose:", player2)
    print("Player 2 wins!!")
elif (player1 == "paper" and player2 == "paper"):
    print("Player 2 chose:", player2)
    print("Tie!!")
elif (player1 == "paper" and player2 == "rock"):
    print("Player 2 chose:", player2)
    print("You win!!")

# Player 1 chooses scissors
elif (player1 == "scissors" and player2 == "scissors"):
    print("Player 2 chose:", player2)
    print("Tie!!")
elif (player1 == "scissors" and player2 == "paper"):
    print("Player 2 chose:", player2)
    print("You win!!")
elif (player1 == "scissors" and player2 == "rock"):
    print("Player 2 chose:", player2)
    print("Player 2 wins!!")

