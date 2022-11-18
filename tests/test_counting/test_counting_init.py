import mathematics.counting as counting


def test_totient():
    assert counting.totient(10) == 3
    assert counting.totient(43) == 41
    assert counting.totient(186) == 59


def test_totient_function():
    assert counting.totient_function(1) == 1
    assert counting.totient_function(5) == 4
    assert counting.totient_function(9) == 6
