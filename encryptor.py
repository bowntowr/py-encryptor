# This project was ENTIRELY human coded by bowntowr on GitHub :)
# This is one of my first projects without vibecoding so there may be bugs!

# Importing necesary stuff
import random

# Initially setting variables
ALLOWED_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
key = ""

# Asks the user what they want to encrypt
to_encrypt = input("Enter the string you would like to encrypt: ")

# Finds length of the input string to generate a key
length = len(to_encrypt)

for _ in range(length):
    chosen_char = random.choice(ALLOWED_CHARS)
    key += chosen_char

# Prints string to encrypt and generated key
print("The string to be encrypted:", to_encrypt)
print("Key to encrypt string:", key)