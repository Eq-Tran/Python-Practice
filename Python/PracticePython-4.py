# Divisors
# Ethan Tran 11/11/19
# Create a program that asks the user for a number then prints out a list of all the divisors

a = int(input('Choose a number to divide'))
x = list(range(2,a+1))
divisors = []

for i in x:
    if a % i == 0:
        divisors.append(i)

print(divisors)