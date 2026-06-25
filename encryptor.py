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

# Loop to generate key
for _ in range(length):
    chosen_char = random.choice(ALLOWED_CHARS)
    key += chosen_char

# Sets blank encrypted variable to add onto later
encrypted = ""

# Loop to encrypt inputted string
for m_char, k_char in zip(to_encrypt, key):
    combined = (ord(m_char) + ord(k_char)) % 256
    encrypted += chr(combined)

# Prints finalized encrypted string and key
print("Encrypted string:", encrypted)
print("Key:", key)
