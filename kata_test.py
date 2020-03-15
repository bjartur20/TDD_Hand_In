import kata


def test_add_empty_string():
    assert kata.add('') == 0

def test_single_number():
    assert kata.add('1') == 1