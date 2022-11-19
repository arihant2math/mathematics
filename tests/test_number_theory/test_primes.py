from mathematics.number_theory.primes import *


def test_is_prime_wilsons_theorem():
    assert not is_prime_wilsons_theorem(1)
    assert is_prime_wilsons_theorem(2)
    assert is_prime_wilsons_theorem(3)
    assert not is_prime_wilsons_theorem(4)
    assert is_prime_wilsons_theorem(5)
    assert not is_prime_wilsons_theorem(10)
    assert is_prime_wilsons_theorem(11)
    assert not is_prime_wilsons_theorem(93)


def test_is_prime_fermat_little_theorem():
    assert not is_prime_fermat_little_theorem(1)
    assert is_prime_fermat_little_theorem(2)
    assert is_prime_fermat_little_theorem(3)
    assert not is_prime_fermat_little_theorem(4)
    assert is_prime_fermat_little_theorem(5)
    assert not is_prime_fermat_little_theorem(10)
    assert is_prime_fermat_little_theorem(11)
    assert not is_prime_fermat_little_theorem(93)


def test_is_prime():
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(10)
    assert is_prime(11)
    assert not is_prime(93)


def test_prime_gen():
    assert prime_gen(100) == prime_gen(0, 100)


def test_mersenne():
    assert mersenne(3) == 7
    assert mersenne(5) == 31


def test_lucas_lehmer():
    assert lucas_lehmer(7)
    assert lucas_lehmer(31)


def test_lucas_lehmer_gen():
    pass
