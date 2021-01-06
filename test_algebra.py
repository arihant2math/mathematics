import pytest
import algebra
from unittest import TestCase


class FractionTestClass(TestCase):
    """Tests algebra.Fraction"""
    def test_condition(self):
        algebra.Fraction(numerator=1, denominator=2)

    def test_equal(self):
        x = algebra.Fraction(numerator=1, denominator=2)
        y = algebra.Fraction(numerator=1, denominator=2)
        assert x == y

    def test_addition(self):
        x = algebra.Fraction(numerator=1, denominator=4)
        y = algebra.Fraction(numerator=2, denominator=4)
        assert x + y == algebra.Fraction(numerator=3, denominator=4)
