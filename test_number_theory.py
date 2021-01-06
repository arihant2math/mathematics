import pytest
import number_theory
from unittest import TestCase


class IsPrimeTestClass(TestCase):
    def test_is_prime_edge(self):
        x = number_theory.is_prime(1)
        assert x == False

    def test_is_prime_edge_two(self):
        x = number_theory.is_prime(0)
        assert x == False

    def test_is_prime_edge_three(self):
        x = number_theory.is_prime(-1254)
        assert x == False

    def test_is_prime_false(self):
        x = number_theory.is_prime(211)
        assert x == False

    def test_is_prime_true(self):
        x = number_theory.is_prime(751)
        assert x == False


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

    def test_is_prime_false(self):
        x = number_theory.is_prime_wilsons_theorem(211)
        assert x == False

    def test_is_prime_true(self):
        x = number_theory.is_prime_wilsons_theorem(751)
        assert x == False


class IsPrimeFermatsLittleTheoremTestClass:
    def test_is_prime_edge(self):
        x = number_theory.is_prime_fermat_little_theorem(1)
        assert x == False

    def test_is_prime_edge_two(self):
        x = number_theory.is_prime_fermat_little_theorem(0)
        assert x == False

    def test_is_prime_edge_three(self):
        x = number_theory.is_prime_fermat_little_theorem(-1254)
        assert x == False

    def test_is_prime_false(self):
        x = number_theory.is_prime_fermat_little_theorem(211)
        assert x == False

    def test_is_prime_true(self):
        x = number_theory.is_prime_fermat_little_theorem(751)
        assert x == False