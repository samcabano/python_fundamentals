import sys

# collatz sequence function
def collatz(number):
    
    # if number is even, divides by 2
    if number % 2 == 0:
        print (number // 2)
        return number // 2

    # if number is odd, multiplies by 3 and adds 1
    elif number % 2 == 1:
        print (3 * number + 1)
        return 3 * number + 1

print ('Enter number: ')

# if input is integer, run collatz, if not, print error message
try:
    num = int(input())
except ValueError:
    print ('ERROR: Invalid value, please enter an integer.')
    sys.exit() 

# runs collatz seq function while returned value is not 1
while num != 1:
    num = collatz (num)
