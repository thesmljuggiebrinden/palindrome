import re

user_input = input("Enter a word or two: ")

def palindrome(a_string):
    a_string = a_string.lower().replace(' ', ' ') # this method ignores uppercase letters
    a_string = re.sub(r'[^a-zA-Z]', '', a_string)
    return a_string == a_string[::-1] # reverses a string

print(palindrome(user_input))


    
