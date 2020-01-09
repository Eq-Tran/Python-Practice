# Python Practice 
# Exercise 15
# Ethan Tran
# 12/8/19
#
# Create a function that returns a long string backwards


a = input("Enter a string to reverse")

def reverseOrder(a):

    b = a.split()
    result = " ".join(b)
    return(result[::-1])

print(reverseOrder(a))