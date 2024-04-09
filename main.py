import random
"""Allows generate_secret_number generates a random number with random module"""

LOWER_NUMBER = 1
UPPER_NUMBER = 100

def generate_secret_number(lower_number, upper_number):
    """Generates a random number with randint that uses as parms lower_number & upper_number"""
    return random.randint(lower_number, upper_number)

def user_guess(lower_number, upper_number):
    """Picks user input and manages errors."""
    while True:
        try:
            guess = int(input(f"Let's start! Guess a number between {lower_number} and {upper_number}:  "))
            if validate_user_input(guess, lower_number, upper_number):
                return guess
            print("Ups! You guessed out of limits. Please, enter a number between 1 and 100. \n \n")
        except ValueError:
            print('Is that a number? Please, try again!\n \n')

def computer_guess(lower_number, upper_number):
    """Generates a random number by computer."""
    return random.randint(lower_number, upper_number)

def validate_user_input(guess, lower_number, upper_number):
    """Returns guessed number if it is ok in terms of limits."""
    return lower_number <= guess <= upper_number

def check_guess(guess, secret_number):
    """Return a message depending on the guessed number."""
    if guess == secret_number:
        return 'Correct'
    if guess < secret_number:
        return 'Too low \n \n'
    return 'Too high \n \n'

def ask_if_want_to_play_again(answer):
    """Asks player if want to play again or not."""
    answer = input("Do you want to play again? (Y/n)")
    answer = str.lower(answer).strip()
    if answer == '' or answer == 'y' or answer == 'yes':
        answer = True
    else:
        answer = False
    return answer

def game(lower_number, upper_number, answer = True):
    """Runs the game by calling methods described above."""
    if answer == False:
        print("See you later!")
        return
    attemps = 0
    user_number_attemps = []
    computer_number_attemps = []
    secret_number = generate_secret_number(lower_number, upper_number)
    while True:
        attemps += 1
        guess1 = user_guess(lower_number, upper_number)
        user_number_attemps.append(guess1)
        result1 = check_guess(guess1, secret_number)
        guess2 = computer_guess(lower_number, upper_number)
        computer_number_attemps.append(guess2)
        result2 = check_guess(guess2, secret_number)
        if result1 == 'Correct':
            print(f"Wow, you're so smart! You guessed the secret number {secret_number} in {attemps} attemps.")
            print(f"Your guesses were {",".join(map(str, user_number_attemps))} \n \n")
            answer = ask_if_want_to_play_again(answer)
            game(lower_number, upper_number, answer)
            break
        print(result1)
        print("Now it is Computer turn!")
        if result2 == 'Correct':
            print(f"Wow, you're so smart! You guessed the secret number {secret_number} in {attemps} attemps.")
            print(f"Your guesses were {",".join(map(str, computer_number_attemps))} \n \n")
            answer = ask_if_want_to_play_again(answer)
            game(lower_number, upper_number, answer)
            break
        print(guess2)
        print(result2)
        print("It is your turn!")

if __name__ == "__main__":
    print("Hi, there! Welcome to Guess the Number Game! \n \n")
    game(LOWER_NUMBER, UPPER_NUMBER, answer= True)
