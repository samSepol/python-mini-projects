import random
import string
print('Welcome to PasswordHasher to generate complex password')

passChar = int(input('What number of character you want to  generate !\n'))
numberOfSymbols = int(input('How many symbols you want to add !\n'))
numLength = int(input('How many numbers you want to add !\n'))

# generate password
password = ""


# genearate characters

for char in range(1, passChar+1):
    password += random.choice(string.ascii_lowercase + string.ascii_uppercase)

# genate symbol

for symbol in range(1, numberOfSymbols+1):
    password += random.choice(string.punctuation)

# geneate numbers

for number in range(1, numLength+1):
    password += random.choice(string.digits)

generated_password = password
print(f'Your generated password is {generated_password} \n')

print(len(generated_password))
