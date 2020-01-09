# List less than ten
# Ethan Tran 11/11/19
# Given a list print the elements that are less than 5

a = [1,1,2,3,5,13,21,34,55,89]
n = []
# This prints out elements < 5 WITH no duplicates
for i in set(a):
    if i <= 5:
 
        n.append(i)
print(n)