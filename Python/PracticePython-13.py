# Fibonacci - exercise 13
# Ethan Tran
# Write a program that asks the user how many fibonacci numbers to generate
# then generates them. Make sure to ask the user to enter the number of numbers in the sequence
# Fibnacci sum = the sum of the last two number ex.) 3 = 1 + 2; 5 = 3 + 2; 8 = 5 + 3

#num = int(input("enter the number of fibonacci numbers to generate"))

######################################
#start = 1                           # -> This was my starting algorithm (Was close!)
#                                    #
#sum = (start - 1) + (start + 1)     #
#print(sum)                          #
######################################

# Fibonacci = Fn = Fn-1 + Fn-2

fibarray = [0,1]

def fib_sequence(n):
    if n <0:
        print('Incorrect input')
    elif n <= len(fibarray):
        return fibarray[n-1]
    else:
        temp_fib = fib_sequence(n-1) + fib_sequence(n-2)
        print(temp_fib)
        fibarray.append(temp_fib)
        print(fibarray)
        return temp_fib

n = int(input('Enter a the number of fibonacci numbers to calculate'))

print(fib_sequence(n))

# MOdify this to show all the numbers 
