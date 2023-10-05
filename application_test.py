import unittest
from application import map


class TestMap(unittest.TestCase):
    """Contains a valid test case for the Map function."""

    def test_map(self):
        nums = [1, 2, 3]
        doubled_nums = [2, 4, 6]
        self.assertEqual(doubled_nums, map(nums))
