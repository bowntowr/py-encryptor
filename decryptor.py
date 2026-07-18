# This project was ENTIRELY human coded by bowntowr on GitHub :) https://github.com/bowntowr
# This is one of my first projects without vibecoding so there may be bugs and there will be MANY COMMENTS while I'm still learning :)
# This is the decryptor script to accompany the encryptor.py file, it will decrypt the string you give it and output it to the terminal

# Importing necesary stuff
import base64

# Sets variables to add onto later
decrypted = ""

# Asks the user what they want to decrypt as well as the key to decrypt it with
to_decrypt = input("Enter the string you would like to decrypt: ")
key = input("Enter the key to decrypt the string with: ")

# Decodes with base64 to get the original encrypted string
to_decrypt = base64.b64decode(to_decrypt.encode("utf-8")).decode("utf-8")

# Checks key length to make sure it matches the string length, if not it will exit the program
if len(to_decrypt) != len(key):
    print("The key length does not match the string length, please try again with the correct key.")
    input("\nPress enter to exit...")
    exit()

# Decrypts the string using the key given by the user
for m_char, k_char in zip(to_decrypt, key):
    combined = (ord(m_char) - ord(k_char)) % 256

    decrypted += chr(combined)

# Prints finalized decrypted string
print("Decrypted string:", decrypted)

# Waits to exit so the user can see the output (otherwise the terminal will instantly close on Windows, linux is fine tho cuz linux is epic)
input("\nPress enter to exit...")