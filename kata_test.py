import kata

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