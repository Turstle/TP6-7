from romains_decoder import *


def calculatrice(firstRomainNumber, secondRomainNumber, symbol):
    if symbol == "+":
        return add(firstRomainNumber, secondRomainNumber)
    if symbol == "-":
        return substract(firstRomainNumber, secondRomainNumber)


def add(firstRomainNumber, secondRomainNumber):
    return decoder(firstRomainNumber) + decoder(secondRomainNumber)


def substract(firstRomainNumber, secondRomainNumber):
    return decoder(firstRomainNumber) - decoder(secondRomainNumber)