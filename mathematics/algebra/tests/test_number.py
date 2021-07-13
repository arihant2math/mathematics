import pytest
from mathematics.algebra.Number import Number


class TestNumber:
    def test_eq(self):
        assert Number(12) == Number(12)

    def test_digit_sum(self):
        assert Number(15124).digit_sum() == 13

    def test_digit_product(self):
        assert Number(25).digit_product() == 10
