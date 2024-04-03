#I need import random module

import random

#I need to asign the range and maximum attemps

lowerNumber = 1
upperNumber = 100

#I need to generate a random number with lower and upper values

secretNumber = random.randint(lowerNumber,upperNumber)
print('Random number is % s' % (secretNumber))
#computerGuess = random.randint()

#Create user input and validation when having an incorrect/invalid input

def userGuess():
    while True:
        try:
            guess = int(input(f"Enter a number between {lowerNumber} and {upperNumber}: "))
            if lowerNumber <= guess <= upperNumber:
               return guess
            else:
                print('Incorrect input. Please, enter a number between 1 and 100, inclusive. \n \n')
        except ValueError:
            print('Incorrect input. Please, enter a valid number.\n \n')

#Create computer input

def computerGuess():
    computerGuess = random.randint(lowerNumber, upperNumber)
    return computerGuess

#User input guess validation
            
def checkGuess(guess, secretNumber):
    if guess == secretNumber:
        return 'Correct'
    elif guess < secretNumber:
        return 'Too low \n \n'
    else:
       return 'Too high \n \n'


def game(answer = True):
    if answer == False:
        print("See you later!")
        return

    attemps = 0
    userNumberAttemps = []
    computerNumberAttemps = []

    while True:
        attemps += 1

        guess1 = userGuess()
        userNumberAttemps.append(guess1)
        result1 = checkGuess(guess1, secretNumber)
        guess2 = computerGuess()
        computerNumberAttemps.append(guess2)
        result2 = checkGuess(guess2, secretNumber)

        if result1 == 'Correct':
            print(f"Congrats! You guessed the secret number {secretNumber} in {attemps} attemps.")
            print(f"Your numbers were {",".join(map(str, userNumberAttemps))} \n \n")
            answer = askIfWantToPlayAgain(answer)
            game(answer)
            break
        else:
            print(result1)
            print("It is Computer turn!")
                      
        if result2 == 'Correct':
            print(f"Congrats! You guessed the secret number {secretNumber} in {attemps} attemps.")
            print(f"Your numbers were {",".join(map(str, computerNumberAttemps))} \n \n")
            answer = askIfWantToPlayAgain(answer)
            game(answer)
            break
        else:
            print(guess2)
            print(result2)
            print("It is User turn!")

def askIfWantToPlayAgain(answer):
    answer = input("Do you want to play again? (Y/n)")
    answer = str.lower(answer).strip()
    if answer == '' or answer == 'y' or answer == 'yes':
        answer = True
    else:
        answer = False
    return answer

    #if not winner:
        #print(f"Sorry, you ran out of attemps! The secret number is {secretNumber}.")

if __name__ == "__main__":
    print("Welcome to Guess the Number game! \n \n")
    game()

