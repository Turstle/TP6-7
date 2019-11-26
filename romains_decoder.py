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


def decoder_n_identical_chars(nIdenticalChars):
    n = len(nIdenticalChars)
    if nIdenticalChars[0] == 'I':
        return decoder_one_char('I') * n
    if nIdenticalChars[0] == 'V':
        return decoder_one_char('V') * n
    if nIdenticalChars[0] == 'X':
        return decoder_one_char('X') * n
    if nIdenticalChars[0] == 'L':
        return decoder_one_char('L') * n
    if nIdenticalChars[0] == 'C':
        return decoder_one_char('C') * n
    if nIdenticalChars[0] == 'D':
        return decoder_one_char('D') * n
    if nIdenticalChars[0] == 'M':
        return decoder_one_char('M') * n