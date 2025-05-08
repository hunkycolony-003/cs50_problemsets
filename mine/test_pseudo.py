from pseudo import check

def test_check():
    assert check(12) == False
    assert check(22022) == True
    assert check(0) == True
    assert check(234) == False
