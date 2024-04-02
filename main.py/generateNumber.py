#I need import random module

import random

#I need to asign the range

lowerNumber = 1
upperNumber = 100
maxAttemp = 3

#I need to generate a random number with lower and upper values

secretNumber = random.randint(lowerNumber,upperNumber)
#print('Random number is % s' % (secretNumber))
#computerGuess = random.randint()

#Create user input and validation when having an incorrect/invalid input

def userGuess():
    while True:
        try:
            guess = int(input(f"Enter a number between {lowerNumber} and {upperNumber}: "))
            if lowerNumber <= guess <= upperNumber:
               return guess
            else:
                print('Incorrect input. Please, enter a number between 1 and 100, inclusive.')
        except ValueError:
            print('Incorrect input. Please, enter a valid number.')

#Create computer input

def computerGuess():
    computerGuess = random.randint(lowerNumber, upperNumber)
    return computerGuess

#User input guess validation
            
def checkUserGuess(guess, secretNumber):
    if guess == secretNumber:
        return 'Yes, you win'
    elif guess < secretNumber:
        return 'Too low'
    else:
       return 'Too high'

#Computer input guess validation
            
def checkComputerGuess(computerGuess, secretNumber):
    if computerGuess == secretNumber:
        return 'Yes, you win'
    elif computerGuess < secretNumber:
        return 'Too low'
    else:
       return 'Too high'

userGuess()
computerGuess()
checkUserGuess()
checkComputerGuess()
