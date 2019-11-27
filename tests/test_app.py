from romains_decoder import *
from calculatrice import *

def test_decoder_for_one_char():
    assert decoder('I') == 1
    assert decoder('V') == 5
    assert decoder('X') == 10
    assert decoder('L') == 50
    assert decoder('C') == 100
    assert decoder('D') == 500
    assert decoder('M') == 1000


def test_decoder_for_two_identical_chars():
    assert decoder("II") == 2
    assert decoder("VV") == 10
    assert decoder("XX") == 20
    assert decoder("LL") == 100
    assert decoder("CC") == 200
    assert decoder("DD") == 1000
    assert decoder("MM") == 2000


def test_decoder_for_n_identical_chars():
    assert decoder("III") == 3
    assert decoder("VVVV") == 20
    assert decoder("XXXXX") == 50
    assert decoder("LLLLLL") == 300
    assert decoder("CCCCCCC") == 700
    assert decoder("DDDDDDDD") == 4000
    assert decoder("MMMMMMMMM") == 9000


def test_decoder_for_no_substract_string():
    assert decoder("VI") == 6
    assert decoder("LX") == 60
    assert decoder("DC") == 600
    assert decoder("MD") == 1500


def test_decoder_of_string_with_substractions():
    assert decoder("IV") == 4
    assert decoder("XIV") == 14
    assert decoder("MCMXLIV") == 1944


def test_calculatrice_add():
    assert calculatrice("X","X","+") == 20


def test_calculatrice_substract():
    assert calculatrice("X", "X", "-") == 0


def test_calculatrice_multiply():
    assert calculatrice("X", "X", "*") == 100

def test_calculatrice_divide():
    assert calculatrice("X", "X", "/") == 1
    assert calculatrice("IV", "II", "/") == 2