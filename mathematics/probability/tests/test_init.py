import unittest
from mathematics import probability
from mathematics.algebra.Fraction import Fraction


class TestProbability(unittest.TestCase):
    def test_value(self):
        self.assertEqual(probability.Probability([1, 2, 3], [1, 2, 3, 4, 5, 6]).value(),
                         Fraction(numerator=1, denominator=3))

    def test_compliment(self):
        self.assertEqual(probability.Probability([1, 2, 3, 4], [1, 2, 3, 4, 5, 6]).complement(),
                         Fraction(numerator=1, denominator=3))


if __name__ == '__main__':
    unittest.main()
