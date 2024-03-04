from asyncio import run
import string

def recursive_password(value: str):
    password = ""
    find = False
    for count, valeur in enumerate(string.ascii_letters):
        password = value
        if password[0] == valeur:
            find = True
            return password
        elif count == 26 and find == False:
            for i in 


def get_password(value: str):
    password = ""
    find = False
    recursive_password(value)



