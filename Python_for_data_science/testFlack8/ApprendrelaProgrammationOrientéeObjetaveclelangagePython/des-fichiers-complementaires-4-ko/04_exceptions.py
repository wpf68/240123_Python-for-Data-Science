import re

class EntreeIncorrecte(BaseException): pass
class EmailMalFormate(BaseException): pass
class CyberAttaque(BaseException): pass

def validation_email(chaine):
    if chaine is None or chaine == "":
        raise EntreeIncorrecte
    if re.search(".*@.*\..*", chaine) is None:
        raise EmailMalFormate
    if chaine != "vincent@eni.fr":
        raise CyberAttaque

attaque = False
while not attaque:
    try:
        chaine = input('--> ')
        validation_email(chaine)
        # Si l'on arrive à cette ligne, cela veut dire qu'aucune
        # exception n'a été levée. Par conséquent, l'email est correct
        # et la boucle peut être brisée.
        break
    except EntreeIncorrecte:
        print("'{}' est une entrée incorrecte. Saisissez une adresse e-mail".format(chaine))
    except EmailMalFormate:
        print("Une adresse e-mail doit être de la forme xxx@xxx.xx")
    except CyberAttaque:
        print("Compte bloqué pour cause d'attaque")
        attaque = True
if not attaque:
    print("Bienvenue Vincent!")
