def decoder(romainNumber):
    if romainNumber == 'I':
        return 1
    elif romainNumber == 'V':
        return 5
    elif romainNumber == 'X':
        return 10
    elif romainNumber == 'L':
        return 50
    elif romainNumber == 'C':
        return 100
    elif romainNumber == 'D':
        return 500
    elif romainNumber == 'M':
        return 1000
    else:
        result_of_conversion = 0
        for letterIndex in range (0, len(romainNumber)):
            if check_if_previous_number_is_lower(romainNumber, letterIndex):
                result_of_conversion = result_of_conversion - 2 * decoder(romainNumber[letterIndex - 1])
                result_of_conversion = result_of_conversion + decoder(romainNumber[letterIndex])
            else:
                result_of_conversion = result_of_conversion + decoder(romainNumber[letterIndex])
        return result_of_conversion


def check_if_previous_number_is_lower(romainNumber, letterIndex):
    if decoder(romainNumber[letterIndex - 1]) < decoder(romainNumber[letterIndex]) and letterIndex != 0:
        return True
    else:
        return False