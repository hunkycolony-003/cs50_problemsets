from um import count


def test_sub():
    assert count("annum") == 0
    assert count("Umbrella") == 0


def test_case():
    assert count("Umm, you are right") == 0
    assert count("Um, you are right") == 1
    assert count("uM, you are UM, right") == 2


def test_suffix():
    assert count("um you are right") == 1
    assert count("Um... you are right") == 1
    assert count("Um? what did you say") == 1
