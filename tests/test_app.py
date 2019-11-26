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


def test_decoder_for_two_identical_chars():
    assert decoder_two_identical_chars("II") == 2
    assert decoder_two_identical_chars("VV") == 10
    assert decoder_two_identical_chars("XX") == 20
    assert decoder_two_identical_chars("LL") == 100
    assert decoder_two_identical_chars("CC") == 200
    assert decoder_two_identical_chars("DD") == 1000
    assert decoder_two_identical_chars("MM") == 2000


def test_decoder_for_n_identical_chars():
    assert decoder_n_identical_chars("III") == 3
    assert decoder_n_identical_chars("VVVV") == 20
    assert decoder_n_identical_chars("XXXXX") == 50
    assert decoder_n_identical_chars("LLLLLL") == 300
    assert decoder_n_identical_chars("CCCCCCC") == 700
    assert decoder_n_identical_chars("DDDDDDDD") == 4000
    assert decoder_n_identical_chars("MMMMMMMMM") == 9000


