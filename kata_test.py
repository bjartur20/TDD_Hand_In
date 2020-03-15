import kata
import pytest

# 1
def test_add_empty_string():
    assert kata.add('') == 0

# 2
def test_single_number():
    assert kata.add('1') == 1

# 3
def test_two_numbers():
    assert kata.add('1,2') == 3

# 4
def test_unknown_number_of_numbers():
    assert kata.add('1,2,3,4,5') == 15
    assert kata.add('10,2,5,22,1,1') == 41

# 5
def test_newline_instead_of_comma():
    assert kata.add('1,2\n3') == 6

# 6
def test_ignore_bigger_than_1000():
    assert kata.add('1001,2') == 2

# 7
def test_error_negative():
    with pytest.raises(kata.NegativeError, match='Negatives not allowed: -1'):
        kata.add('-1,2')

    with pytest.raises(kata.NegativeError, match='Negatives not allowed: -4,-5'):
        kata.add('2,-4,3,-5')

# 8
def test_different_delimeter():
    assert kata.add('//X\n1X2') == 3
    assert kata.add('//%\n1%2%3') == 6
    