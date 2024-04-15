import string
import time


def recursiveMdp(longueurMdp: int, listChar: list[str], longueurActuelle: int = 1, oldMdp: str = ''):
    for char in listChar:
        nvMdp = oldMdp + char
        if longueurActuelle == longueurMdp:
            print(nvMdp)
        else:
            recursiveMdp(longueurMdp, listChar, longueurActuelle + 1, oldMdp)


timeDebut = time.time()
longueurMdp = 5

listNum = string.digits
listLowercase = string.ascii_lowercase
listUppercase = string.ascii_uppercase
listSpecial = string.punctuation
listUsedChoix = ["Numeric", "Lowercase Letters",
                 "Uppercase Letters", "Special characters"]
timeFin = time.time()
print(f"le programme a duré {timeFin - timeDebut} secondes")
