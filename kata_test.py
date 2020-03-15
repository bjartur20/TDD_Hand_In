import kata

def test_add_empty_string():
    assert kata.add('') == 0

def test_single_number():
    assert kata.add('1') == 1

def test_two_numbers():
    assert kata.add('1,2') == 3

def test_unknown_number_of_numbers():
    assert kata.add('1,2,3,4,5') == 15
    assert kata.add('10,2,5,22,1,1') == 41