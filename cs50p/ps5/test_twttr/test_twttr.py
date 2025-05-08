from twttr import shorten


def test_capital():
    assert shorten("UMBRELLA") == "MBRLL"
    assert shorten("OASIS") == "SS"
    assert shorten("IOUEA") == ""


def test_small():
    assert shorten("umbrella") == "mbrll"
    assert shorten("oasis") == "ss"
    assert shorten("iouea") == ""


def test_mixed():
    assert shorten("UmbRElLA") == "mbRlL"
    assert shorten("OaSIs") == "Ss"
    assert shorten("IoUEa") == ""


def test_num():
    assert shorten("Dee2er") == "D2r"


def test_punc():
    assert shorten("HI!") == "H!"
