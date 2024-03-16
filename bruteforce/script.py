import enum
import os
import string
import webbrowser
import sqlite3


class PasswordChoice(enum.Enum):
    MINUSCULE = "minus"
    MAJUSCULE = "maj"
    NUMERIQUE = "numeric"
    TOUT = "tout"


class PasswordBruteforce:
    def reset_password_db(self):
        db = sqlite3.connect("./database/db.sqlite")
        curseur = db.cursor()
        curseur.execute("DELETE FROM config")
        db.commit()
        db.close()

    def recursive_password(self, longueurPwd: int, listChars: list[str | int] | list[int] | list[str], save_possibilities: str, longueurActuelle=1, oldPwd=""):
        if bool(save_possibilities) == True:
            db = sqlite3.connect("./database/db.sqlite")
            curseur = db.cursor()
        for char in listChars:
            newPwd = oldPwd + str(char)
            curseur.execute(f"INSERT INTO config VALUES ('{newPwd}')")
            db.commit()
            if bool(save_possibilities) == False:
                print(newPwd)
            if longueurActuelle == longueurPwd:
                pass
            else:
                self.recursive_password(
                    longueurPwd, listChars, save_possibilities, longueurActuelle + 1, newPwd)
        db.commit()
        db.close()

    def get_password(self, Pwd: str = input("Donnez le mot de passe que vous voulez chercher : "), choix: str = input("quel est le type de caractères du mot de passe ? "), save_possibilities=input("voulez-vous sauvegarder les possibilités de chaque itérations dans une base de données ? "), /, *args: tuple[str, str, str]):
        save_possibilities = save_possibilities.casefold().replace(
            "non", "False").replace("oui", "True")

        listUsed = []
        longueurMdp = len(Pwd)
        listeNum = [int(num) for num in string.digits]
        listeLettreMinuscules = [lettre for lettre in string.ascii_lowercase]
        listeLettreMajuscules = [lettre for lettre in string.ascii_uppercase]
        listeCharSpeciaux = [ponctuation for ponctuation in string.punctuation]
        userChoices = (Pwd, choix, save_possibilities)
        choixCasefold = choix.casefold()

        if choixCasefold == PasswordChoice.MINUSCULE.value:
            listUsed = listeLettreMinuscules
        if choixCasefold == PasswordChoice.MAJUSCULE.value:
            listUsed = listeLettreMajuscules
        if choixCasefold == PasswordChoice.NUMERIQUE.value:
            listUsed = listeNum
        if choixCasefold == PasswordChoice.TOUT.value:
            listUsed = listeLettreMinuscules + \
                listeLettreMajuscules + listeNum + listeCharSpeciaux

        self.recursive_password(
            longueurMdp, listUsed, save_possibilities, 1, "")


bruteforce = PasswordBruteforce()
bruteforce.reset_password_db()
