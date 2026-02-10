import hashlib as h
from colorama import Fore, Style, Back
def hash():
    target = input("enter hashed password:")
    f1 = open("input.txt" , "r")
    text = f1.readlines()
    for i in range(len(text)):
        password = text[i].strip("\n")
        hashed = h.sha512(password.encode()).hexdigest()
        if hashed == target:
            print("Hash Decrypted:", hashed , "\n input password:", password)

hash()