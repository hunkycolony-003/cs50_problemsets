import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("1/4") == 25
    assert convert("2/3") == 67


def test_Error():
    with pytest.raises(ZeroDivisionError):
        convert("23/0")
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("YTRN")
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_gauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(23) == "23%"
    assert gauge(2) == "2%"
