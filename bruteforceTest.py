import hashlib
import itertools
import os
import string


def cracker_mot_de_passe():
    """
    Fonction pour cracker un mot de passe haché par force brute.

    Args:
        mot_de_passe_hache: Le mot de passe haché à cracker.
        ensemble_caracteres: L'ensemble de caractères possibles pour le mot de passe.
        longueur_max: La longueur maximale du mot de passe.

    Returns:
        Le mot de passe clair s'il est trouvé, None sinon.
    """

    ensemble_caracteres, mot_de_passe_hache, longueur_max = choixUtilisateur()
    for longueur in range(1, longueur_max + 1):
        for combinaison in itertools.product(ensemble_caracteres, repeat=longueur):
            mot_de_passe_essai = "".join(combinaison)
            mot_de_passe_hache_essai = hashlib.sha256(
                mot_de_passe_essai.encode()).hexdigest()
            saveFileExists = os.path.join(
                os.path.dirname(__file__), 'essais_mdp.txt')
            if saveFileExists:
                with open(saveFileExists, 'a') as file:
                    if mot_de_passe_hache_essai == mot_de_passe_hache:
                        print(
                            f"Mot de passe trouvé : \"{mot_de_passe_essai}\"")
                        return
                    else:
                        file.write(f"{mot_de_passe_essai} ;" +
                                   " " if longueur + 1 != longueur else "")
    return None


def choixUtilisateur():
    mot_de_passe_hache_clair = input(
        f"entre un petit mots de passe max 8 caractères en alphanumérique : ")

    longueur_max = len(mot_de_passe_hache_clair)
    mot_de_passe_hache = hashlib.sha256(
        mot_de_passe_hache_clair.encode()).hexdigest()
    print("quel type de caractères compose ce mot de passe ? ")
    textPossibilites = ["Alphanumérique", "Numérique",
                        "Minuscules", "Majuscules", "Tout"]
    for position, possibility in enumerate(textPossibilites):
        print(f"{position + 1} : {possibility}")
    userChoice = int(input())
    ensemble_caracteres = ""
    if userChoice == 1:
        ensemble_caracteres = string.ascii_letters + string.digits
    elif userChoice == 2:
        ensemble_caracteres = string.digits
    elif userChoice == 3:
        ensemble_caracteres = string.ascii_lowercase
    elif userChoice == 4:
        ensemble_caracteres = string.ascii_uppercase
    elif userChoice == 5:
        ensemble_caracteres = string.ascii_letters + string.digits + string.punctuation

    return ensemble_caracteres, mot_de_passe_hache, longueur_max


# Exemple d'utilisation
cracker_mot_de_passe()
