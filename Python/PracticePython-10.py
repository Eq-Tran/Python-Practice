# Practice Python Exercise 10
# List Overlap Comprehensions
# Ethan Tran 11/12/19
# Take two lists and return the common elements between those two lists ( without duplicates)
# BONUS: DO it in as little lines as possible
# note: The question was not possible without using a set due to writer error of the problem 
# note: I did the problem fine BUT used google for the BONUS

a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
n = []
# Multiple Lines
for i in set(a):
    if i in b:
        n.append(i)
       
print(n)

# One line
newer = [i for i in set(a) if i in b]
print(newer)


