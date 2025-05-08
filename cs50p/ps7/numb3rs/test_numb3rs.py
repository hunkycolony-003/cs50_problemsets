from numb3rs import validate


def test_alphanum():
    assert validate("rty.y9.p2u.poi") == False
    assert validate("ytre78dv9") == False


def test_punc():
    assert validate("234556765") == False
    assert validate("54.6567854") == False
    assert validate("54:43:98:89") == False


def test_out_of_range():
    assert validate("256.12.21.32") == False
    assert validate("212.212.273.321") == False


def test_validate_correct():
    assert validate("0.0.0.0") == True
    assert validate("34.32.112.54") == True
    assert validate("123.213.113.253") == True
    assert validate("255.255.255.255") == True
