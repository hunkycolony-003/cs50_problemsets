from bank import value


def test_zero():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("HelLo") == 0


def test_twenty():
    assert value("hi") == 20
    assert value("hllo") == 20
    assert value("Hush") == 20


def test_hundred():
    assert value("bonjour") == 100
    assert value("namaste") == 100
    assert value("what's up!") == 100
