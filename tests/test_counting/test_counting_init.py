import mathematics.counting as counting


def test_totient():
    assert counting.totient(10) == 3
    assert counting.totient(43) == 41
    assert counting.totient(186) == 59

def test_partition():
    assert counting.partition(10)
