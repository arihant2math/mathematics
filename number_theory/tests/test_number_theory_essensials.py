import unittest
from number_theory import number_theory_essensials as number_theory


class TestIsPrimeWilsonsTheorem(unittest.TestCase):
    def test_wilsons_theorem_true(self):
        self.assertEqual(number_theory.is_prime_wilsons_theorem(7043), True)

    def test_wilsons_theorem_false(self):
        self.assertEqual(number_theory.is_prime_wilsons_theorem(6304), False)

    def test_wilsons_theorem_for_zero(self):
        self.assertEqual(number_theory.is_prime_wilsons_theorem(0), False)

    def test_wilsons_theorem_for_one(self):
        self.assertEqual(number_theory.is_prime_wilsons_theorem(1), False)


class TestIsPrimeFermatLittleTheorem(unittest.TestCase):
    def test_fermat_little_theorem_true(self):
        self.assertEqual(number_theory.is_prime_fermat_little_theorem(7043), True)

    def test_fermat_theorem_false(self):
        self.assertEqual(number_theory.is_prime_fermat_little_theorem(6304), False)

    def test_fermat_theorem_for_zero(self):
        self.assertEqual(number_theory.is_prime_fermat_little_theorem(0), False)

    def test_fermat_theorem_for_one(self):
        self.assertEqual(number_theory.is_prime_fermat_little_theorem(1), False)


class TestIsPrime(unittest.TestCase):
    def test_is_prime_true(self):
        self.assertEqual(number_theory.is_prime(7043), True)

    def test_is_prime_false(self):
        self.assertEqual(number_theory.is_prime(6304), False)

    def test_is_prime_for_zero(self):
        self.assertEqual(number_theory.is_prime(0), False)

    def test_is_prime_for_one(self):
        self.assertEqual(number_theory.is_prime(1), False)


class TestPrimeGen(unittest.TestCase):
    def test_stop(self):
        self.assertEqual(number_theory.prime_gen(10), [2, 3, 5, 7])

    def test_start(self):
        self.assertEqual(number_theory.prime_gen(10, 2), [2, 3, 5, 7])


class LucasLehmer(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
