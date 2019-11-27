from romains_decoder import *


def calculatrice(firstRomainNumber, secondRomainNumber, symbol):
    if symbol == "+":
        return add(firstRomainNumber, secondRomainNumber)
    if symbol == "-":
        return substract(firstRomainNumber, secondRomainNumber)
    if symbol == "*":
        return multiply(firstRomainNumber, secondRomainNumber)
    if symbol == "/":
        return divide(firstRomainNumber, secondRomainNumber)

def add(firstRomainNumber, secondRomainNumber):
    return decoder(firstRomainNumber) + decoder(secondRomainNumber)


def substract(firstRomainNumber, secondRomainNumber):
    return decoder(firstRomainNumber) - decoder(secondRomainNumber)


def multiply(firstRomainNumber, secondRomainNumber):
    return decoder(firstRomainNumber) * decoder(secondRomainNumber)


def divide(firstRomainNumber, secondRomainNumber):
    return decoder(firstRomainNumber) / decoder(secondRomainNumber)