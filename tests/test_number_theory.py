import pytest
import ./number_theory


class IsPrimeTestClass:
    def test_is_prime_edge(self):
        x = number_theory.is_prime(1)
        assert x == False

    def test_is_prime_edge_two(self):
        x = number_theory.is_prime(0)
        assert x == False

    def test_is_prime_edge_three(self):
        x = number_theory.is_prime(-1254)
        assert x == False

    def test_is_prime(self):
        x = number_theory.is_prime(37871)
        assert x == True

class IsPrimeWilsonsTheoremTestClass:
    def test_is_prime_edge(self):
        x = number_theory.is_prime_wilsons_theorem(1)
        assert x == False

    def test_is_prime_edge_two(self):
        x = number_theory.is_prime_wilsons_theorem(0)
        assert x == False

    def test_is_prime_edge_three(self):
        x = number_theory.is_prime_wilsons_theorem(-1254)
        assert x == False

    def test_is_prime(self):
        x = number_theory.is_prime_wilsons_theorem(37871)
        assert x == True


class IsPrimeFermatsLittleTheoremTheoremTestClass:
    def test_is_prime_edge(self):
        x = number_theory.is_prime_fermat_little_theorem(1)
        assert x == False

    def test_is_prime_edge_two(self):
        x = number_theory.is_prime_fermat_little_theorem(0)
        assert x == False

    def test_is_prime_edge_three(self):
        x = number_theory.is_prime_fermat_little_theorem(-1254)
        assert x == False

    def test_is_prime(self):
        x = number_theory.is_prime_fermat_little_theorem(37871)
        assert x == True