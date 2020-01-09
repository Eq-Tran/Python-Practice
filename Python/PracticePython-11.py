# Practice Python Exercise 11
# Check for Primality Functions
# Ethan Tran 11/12/19
# Ask the user for a number than determine if the number is prime or not. Use a function to complete this exercise

s = int(input("Choose a nukber to check for primality"))

def check_prime(s):

    num = int(input("number to check divisor by"))
    if s % num == 0:
        print("not prime")
    else:
        print('Prime')

check_prime(s)