from romains_decoder import *
from calculatrice import *


continuer = "oui"
print("Bienvenue sur la calculatrice de nombres Romains!")
while continuer != "non":
    print("Veuillez saisir le symbole de l'opération que vous voulez executer : ") ; symbol = str(input())
    print("Veuillez saisir votre premier nombre romain : ") ; firstRomainNumber = str(input())
    print("Veuillez saisir votre second nombre romain : ") ; secondRomainNumber = str(input())

    if symbol == "+":
        print("La somme de ", firstRomainNumber, " et ", secondRomainNumber, " est égale à ", calculatrice(firstRomainNumber, secondRomainNumber, symbol))
    elif symbol == "-":
        print("La soustraction de ", firstRomainNumber, " à ", secondRomainNumber, " est égale à ", calculatrice(firstRomainNumber, secondRomainNumber, symbol))
    elif symbol == "*":
        print("La multiplication entre ", firstRomainNumber, " et ", secondRomainNumber, " est égale à ", calculatrice(firstRomainNumber, secondRomainNumber, symbol))
    else:
        print("La division de ", firstRomainNumber, " par ", secondRomainNumber, " est égale à ", calculatrice(firstRomainNumber, secondRomainNumber, symbol))
    print("Voulez vous continuer? (oui, non) : ") ; continuer = str(input())
