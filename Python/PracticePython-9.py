# Guessing Game One
# Generate a random number between 1 and 9 including 1 and 9. Have the user guess the number, then tell if they 
# guessed
# too high or too low.
# Ethan Tran 11/11/19

import random

game = True
number = random.randrange(0,10)
guesses = 0
while game == True:
    guesses += 1
    choice = int(input('Guess the number'))

    if choice < number:
        print('Guessed Low')
    elif choice > number:
        print('Guessed High')
    elif choice == number:
        print('Guessed Right ! You WINN')

    again = input('Play again y/n')

    if again == 'Y'.lower():
        game = True
    else:
        game = False
    print('Number of guesses made: ', guesses)