#I need import random module

import random

#I need to asign the range and maximum attemps

lowerNumber = 1
upperNumber = 100
maxAttemp = 5

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
        return 'Correct'
    elif guess < secretNumber:
        return 'Too low'
    else:
       return 'Too high'

#Computer input guess validation
            
def checkComputerGuess(computerGuess, secretNumber):
    if computerGuess == secretNumber:
        return 'Correct'
    elif computerGuess < secretNumber:
        return 'Too low'
    else:
       return 'Too high'

def game():
    attemps = 0
    winner = False

    while attemps <= maxAttemp:
        attemps += 1

        guess1 = userGuess()
        result1 = checkUserGuess(guess1, secretNumber)

        if result1 == 'Correct':
            print(f"Congrats! You guessed the secret number {secretNumber} in {attemps} attemps.")
            winner = True
            break
        else:
            print(f"{result1}. Try again!")
    if not winner:
        print(f"Sorry, you ran out of attemps! The secret number is {secretNumber}.")


    while attemps <=maxAttemp:
         attemps += 1
         guess2 = computerGuess()
         result2 = checkComputerGuess(guess2, secretNumber)
         
         if result2 == 'Yes, you win':
            print(f"Congrats! You guessed the secret number {secretNumber} in {attemps} attemps.")
            winner = True
            break
         else:
            print(f"{result2}. Try again!")

if __name__ == "_main_":
    print("Welcome to Guess the Number game!")
    game()