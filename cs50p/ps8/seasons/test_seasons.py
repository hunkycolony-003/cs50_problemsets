from seasons import get_minutes


def test_all():
    assert get_minutes("2023-07-03") == "Five hundred twenty-seven thousand forty minutes"
    assert get_minutes("2022-07-03") == "One million, fifty-two thousand, six hundred forty minutes"

