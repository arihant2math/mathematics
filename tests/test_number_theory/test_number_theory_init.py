import mathematics.number_theory.primes
from mathematics import number_theory

from mathematics.number_theory import d, partition, lucas_lehmer


def test_is_prime_wilsons_theorem():
    assert not mathematics.number_theory.primes.is_prime_wilsons_theorem(1)
    assert mathematics.number_theory.primes.is_prime_wilsons_theorem(2)
    assert mathematics.number_theory.primes.is_prime_wilsons_theorem(3)
    assert not mathematics.number_theory.primes.is_prime_wilsons_theorem(4)
    assert mathematics.number_theory.primes.is_prime_wilsons_theorem(5)
    assert not mathematics.number_theory.primes.is_prime_wilsons_theorem(10)
    assert mathematics.number_theory.primes.is_prime_wilsons_theorem(11)
    assert not mathematics.number_theory.primes.is_prime_wilsons_theorem(93)


def test_is_prime_fermat_little_theorem():
    assert not mathematics.number_theory.primes.is_prime_fermat_little_theorem(1)
    assert mathematics.number_theory.primes.is_prime_fermat_little_theorem(2)
    assert mathematics.number_theory.primes.is_prime_fermat_little_theorem(3)
    assert not mathematics.number_theory.primes.is_prime_fermat_little_theorem(4)
    assert mathematics.number_theory.primes.is_prime_fermat_little_theorem(5)
    assert not mathematics.number_theory.primes.is_prime_fermat_little_theorem(10)
    assert mathematics.number_theory.primes.is_prime_fermat_little_theorem(11)
    assert not mathematics.number_theory.primes.is_prime_fermat_little_theorem(93)


def test_is_prime():
    assert not mathematics.number_theory.primes.is_prime(1)
    assert mathematics.number_theory.primes.is_prime(2)
    assert mathematics.number_theory.primes.is_prime(3)
    assert not mathematics.number_theory.primes.is_prime(4)
    assert mathematics.number_theory.primes.is_prime(5)
    assert not mathematics.number_theory.primes.is_prime(10)
    assert mathematics.number_theory.primes.is_prime(11)
    assert not mathematics.number_theory.primes.is_prime(93)


def test_prime_gen():
    assert mathematics.number_theory.primes.prime_gen(100) == mathematics.number_theory.primes.prime_gen(0, 100)


def test_mersenne():
    assert mathematics.number_theory.primes.mersenne(3) == 7
    assert mathematics.number_theory.primes.mersenne(5) == 31


def test_lucas_lehmer():
    assert lucas_lehmer(7)
    assert lucas_lehmer(31)


def test_lucas_lehmer_gen():
    pass


def test_prime_factor():
    assert mathematics.number_theory.primes.prime_factor(1) == [1]
    assert mathematics.number_theory.primes.prime_factor(11) == [11]
    assert mathematics.number_theory.primes.prime_factor(100) == [2, 2, 5, 5]


def test_factor():
    assert number_theory.factors(1) == [1]
    assert number_theory.factors(10) == [1, 2, 5, 10]
    assert number_theory.factors(20) == [1, 2, 4, 5, 10, 20]
    assert number_theory.factors(22) == [1, 2, 11, 22]
    assert number_theory.factors(100) == [1, 2, 4, 5, 10, 20, 25, 50, 100]


def test_nth_power():
    assert number_theory.nth_power(3, 3) == [1, 8, 27]


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
    assert partition(4) == [[4], [1, 3], [2, 2], [1, 1, 2], [1, 1, 1, 1]]
