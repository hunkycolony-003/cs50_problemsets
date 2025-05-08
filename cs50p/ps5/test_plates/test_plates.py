from plates import is_valid


def test_1():
    assert is_valid("E223") == False
    assert is_valid("5P776") == False


def test_2():
    assert is_valid("K") == False
    assert is_valid("STHJ4567") == False


def test_3A():
    assert is_valid("HYT67L") == False
    assert is_valid("AA52DF") == False


def test_3B():
    assert is_valid("SSG012") == False
    assert is_valid("SS000") == False


def test_4():
    assert is_valid("AA;TYU") == False
    assert is_valid("AA YTR") == False
    assert is_valid("RTY.87") == False


def test_all_satisfied():
    assert is_valid("AA4567") == True
    assert is_valid("TYUII") == True
    assert is_valid("ERT120") == True
    assert is_valid("ER3") == True
