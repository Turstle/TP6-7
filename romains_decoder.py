def decoder_one_char(romainChar):
    if romainChar == 'I':
        return 1
    if romainChar == 'V':
        return 5
    if romainChar == 'X':
        return 10
    if romainChar == 'L':
        return 50
    if romainChar == 'C':
        return 100
    if romainChar == 'D':
        return 500
    if romainChar == 'M':
        return 1000


def decoder_two_identical_chars(twoIdenticalChars):
    if twoIdenticalChars == "II":
        return decoder_one_char('I') * 2
    if twoIdenticalChars == "VV":
        return decoder_one_char('V') * 2
    if twoIdenticalChars == "XX":
        return decoder_one_char('X') * 2
    if twoIdenticalChars == "LL":
        return decoder_one_char('L') * 2
    if twoIdenticalChars == "CC":
        return decoder_one_char('C') * 2
    if twoIdenticalChars == "DD":
        return decoder_one_char('D') * 2
    if twoIdenticalChars == "MM":
        return decoder_one_char('M') * 2