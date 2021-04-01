import unittest
from mathematics.algebra.Number import Number


class TestNumber(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(Number(12), Number(12))

    def test_digit_sum(self):
        self.assertEqual(Number(15124).digit_sum(), 13)

    def test_digit_product(self):
        self.assertEqual(Number(25).digit_product(), 10)


if __name__ == '__main__':
    unittest.main()
