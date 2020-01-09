# List Ends - Exercise 12
# Ethan Tran 11/12/19
# Write a program that takes a list of numbers and makes a new list of the first and last elements of the list
# Write this code in a function

s = [1,2,3,4,5,6,7]

def list_end(s):

    new = [s[i] for i in (0, -1)]

    return print(new)

list_end(s)