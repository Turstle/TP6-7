from app import *
from romains_decoder import *


def test_decoder_for_one_char():
    assert decoder_one_char('I') == 1
    assert decoder_one_char('V') == 5
    assert decoder_one_char('X') == 10
    assert decoder_one_char('L') == 50
    assert decoder_one_char('C') == 100
    assert decoder_one_char('D') == 500
    assert decoder_one_char('M') == 1000






