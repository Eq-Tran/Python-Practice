# String Lists
# Ethan Tran 11/11/19
# Ask the use for a string and print out whether this string is a palindrome (word that is the same speeled backwards)

s = "dood"

def rev(s):
    return s[::-1]

def isPalindrome(s):

    if rev(s) == s:
        print(s + ' is Palindrome')
    elif rev(s) != s:
        print(s + ' is not Palindrome')

isPalindrome(s)