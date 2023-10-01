import unittest
from application import add, map


class TestCustomMap(unittest.TestCase):

    def test_map(self):
        """ Test the map function with the add function"""
        nums = [1, 2, 3, 4]
        expected_output = [2, 3, 4, 5]
        sum = map(add, nums)
        self.assertEqual(sum, expected_output)


if __name__ == '__main__':
    unittest.main()
