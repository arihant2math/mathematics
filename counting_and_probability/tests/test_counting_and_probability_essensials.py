import unittest
from counting_and_probability import counting_and_probability_essensials


class TestTotient(unittest.TestCase):
    def test_base(self):
        self.assertEqual(counting_and_probability_essensials.totient(10, True), (4, [1, 3, 7, 9]))


if __name__ == '__main__':
    unittest.main()
