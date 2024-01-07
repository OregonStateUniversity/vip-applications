# Author:           Taylor Jordan
# GitHub username:  RangerTJ
# Date:             1/6/2024
# Description:      Sample unit tests for my application's map function.

import unittest
from application import map

test_array = [-2, -1, 0, 1, 2]


# Test functions
def test_sum_func(original_number):
    """Adds 1 to a number and returns the result."""
    return original_number + 1


def test_mult_func(original_number):
    """Multiplies an argument number and returns the result."""
    return original_number * 2


# Unit Tests
class TestCase(unittest.TestCase):

    # Test basic addition function being mapped for an input array
    def test0001(self):
        self.assertTrue(map(test_array, test_sum_func) == [-1, 0, 1, 2, 3])

    # Test basic multiplication function being mapped for an input array
    def test0002(self):
        self.assertTrue(map(test_array, test_mult_func) == [-4, -2, 0, 2, 4])


if __name__ == '__main__':
    unittest.main()
