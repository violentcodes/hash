import supabase
import hashlib as h
import colorama 
from colorama import Fore, Style, Back
from supabase import create_client, Client
url = input(Fore.CYAN+Style.BRIGHT+"enter supabase url:")
key = input(Fore.RED+Style.BRIGHT+"enter api key:")
client = create_client(url,key)

def signup():
    username = input(Fore.MAGENTA+Style.BRIGHT+"enter username:")
    email = input(Fore.YELLOW+Style.BRIGHT+"enter email:")
    rawpassword = input(Fore.LIGHTGREEN_EX+Style.BRIGHT+"enter password:")
    password = h.sha512(rawpassword.encode()).hexdigest()
    response = client.table("auth").insert({"username": username, "email": email, "password":password}).execute()
    print(response)
signup()
