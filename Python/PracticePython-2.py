# Odd or Even
# Ethan Tran 11/11/19
# Ask user for a number and print odd or even depending on the user input

user_input = int(input('Enter a number'))
mod = user_input % 2
if mod > 0:
    print('Odd')
else:
    print('Even')