import unittest
from mathematics import _hold_list as hold
import datetime


class TestHoldList(unittest.TestCase):
    def test_read(self):
        x = hold.HoldList([1, 2, 3, 4], "test_hold_list_one_to_four")
        self.assertEqual(x.read(), [1, 2, 3, 4])

    def test_write(self):
        x = hold.HoldList(
            [1, 2, 3, 4, 5], "test_hold_list" + str(datetime.datetime.now())
        )
        x.write()
        x.read()


if __name__ == "__main__":
    unittest.main()
