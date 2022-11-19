from mathematics.number_theory import *


def test_prime_factor():
    assert prime_factor(1) == [1]
    assert prime_factor(11) == [11]
    assert prime_factor(100) == [2, 2, 5, 5]


def test_factor():
    assert factors(1) == [1]
    assert factors(10) == [1, 2, 5, 10]
    assert factors(20) == [1, 2, 4, 5, 10, 20]
    assert factors(22) == [1, 2, 11, 22]
    assert factors(100) == [1, 2, 4, 5, 10, 20, 25, 50, 100]


def test_nth_power():
    assert nth_power(3, 3) == [1, 8, 27]


def test_d():
    assert d(5, 10)
    assert not d(3, 11)


def test_primitive_root():
    pass


def test_root_equivalents():
    pass


def test_pigeon_hole():
    pass


def test_primitive_roots():
    pass


def test_partition():
    assert partition(4) == [[1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2], [4]]
