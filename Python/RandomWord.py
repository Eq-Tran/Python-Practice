import random


print("hello")
print("Welcome to a Guessing Game")

file = open("words.txt", "r")
contents = file.read()
print(contents)
word = input()
guesses = 0
tries = 5

while guesses != tries:
    if guesses < tries:
        if word in contents:
            print(True)
            break
    word = input()
    guesses += 1
 