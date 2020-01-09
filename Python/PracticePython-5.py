# List Overlap
# Ethan Tran 11/11/19
# Given two lists write a program that returns a list that contains only the 
# elements that are common between the two

import random

a = list(range(0,16))
b = list(range(1,19))
n = []
print(a)
print(b)
for i in set(a):
    if i in b:
        n.append(i)

print(n)