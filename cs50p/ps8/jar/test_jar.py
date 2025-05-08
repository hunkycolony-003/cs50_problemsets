from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-1)
    jar = Jar(9)
    assert jar.capacity == 9
    assert jar.size == 0

def test_str():
    jar = Jar(8)
    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    jar.withdraw(1)
    assert str(jar) == "🍪🍪"


def test_deposit():
    jar = Jar(5)
    with pytest.raises(ValueError):
        jar.deposit(7)
    jar.deposit(2)
    jar.size == 2


def test_withdraw():
    jar = Jar(7)
    with pytest.raises(ValueError):
        jar.withdraw(2)
    jar.deposit(6)
    jar.withdraw(3)
    jar.size == 3

