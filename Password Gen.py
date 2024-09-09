import random

print('Password Generator')

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ83527522906996173263)?_@!$&`#:'

number = input('Amount of passwords to generate: ')
number = int(number)
length = input('Choose your password length: ')
length = int(length)

print('\nHere are your passwords:')
for pwd in range(number):
        passwords = ''
        for c in range(length):
            passwords += random.choice(characters)
        print(passwords)