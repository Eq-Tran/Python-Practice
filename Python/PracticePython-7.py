# Given a list of numbers print a new list of the even elements of the given list
# BONUS: Do it in one line
# Ethan Tran 11/11/19


a = [1,4,9,16,15,36,49,64,81,100]

new = []
# Does function in multiple lines
for i in a:
    if i % 2 == 0:
        new.append(i)

print(new)

#Does function in one line using list comprehension
newer = [i for i in a if i % 2 == 0 ]
print(newer)

