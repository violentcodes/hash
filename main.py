import hashlib as h
from colorama import Fore, Style, Back
def hashSHA512():
    target = input("enter hashed password:")
    f1 = open("input.txt" , "r")
    text = f1.readlines()
    for i in range(len(text)):
        password = text[i].strip("\n")
        hashed = h.sha512(password.encode()).hexdigest()
        if hashed == target:
            print("Hash Decrypted:", hashed , "\n input password:", password)
def hashSHA256():
    target = input("enter hashed password:")
    f1 = open("input.txt" , "r")
    text = f1.readlines()
    for i in range(len(text)):
        password = text[i].strip("\n")
        hashed = h.sha256(password.encode()).hexdigest()
        if hashed == target:
            print("Hash Decrypted:", hashed , "\n input password:", password)
def hashMD5():
    target = input("enter hashed password:")
    f1 = open("input.txt" , "r")
    text = f1.readlines()
    for i in range(len(text)):
        password = text[i].strip("\n")
        hashed = h.md5(password.encode()).hexdigest()
        if hashed == target:
            print("Hash Decrypted:", hashed , "\n input password:", password)
def hashSHA1():
    target = input("enter hashed password:")
    f1 = open("input.txt" , "r")
    text = f1.readlines()
    for i in range(len(text)):
        password = text[i].strip("\n")
        hashed = h.sha1(password.encode()).hexdigest()
        if hashed == target:
            print("Hash Decrypted:", hashed , "\n input password:", password)

def menu():
    print(Fore.RED + Style.BRIGHT + "CHOOSE ALGORITHM TO DECRYPT HASH:")
    print(Fore.CYAN +Style.BRIGHT+ "[1.] SHA256") 
    print(Fore.MAGENTA +Style.BRIGHT+ "[2.] SHA512")
    print(Fore.CYAN +Style.BRIGHT+ "[3.] MD5") 
    print(Fore.MAGENTA + Style.BRIGHT+ "[4.] SHA1")
    ch = int(input(Fore.RED+Style.BRIGHT+"ENTER INTEGER CHOICE:")) 
    if ch == 1:
        hashSHA256()
    if ch == 2:
        hashSHA512()
    if ch == 3:
        hashMD5()
    if ch == 4:
        hashSHA1()
menu()