import unittest
from mathematics import counting


class TestTotient(unittest.TestCase):
    def test_base(self):
        self.assertEqual(counting.totient(10, True), (4, [1, 3, 7, 9]))


class TestPartition(unittest.TestCase):
    def test_base(self):
        self.assertEqual(
            counting.partition(7),
            [
                [7],
                [1, 6],
                [2, 5],
                [3, 4],
                [1, 1, 5],
                [1, 2, 4],
                [1, 3, 3],
                [2, 2, 3],
                [1, 1, 1, 4],
                [1, 1, 2, 3],
                [1, 2, 2, 2],
                [1, 1, 1, 1, 3],
                [1, 1, 1, 2, 2],
                [1, 1, 1, 1, 1, 2],
                [1, 1, 1, 1, 1, 1, 1],
            ],
        )


if __name__ == "__main__":
    unittest.main()
