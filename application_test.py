import unittest
import math
from application import custom_map, to_lower

class customMapTester(unittest.TestCase):
    """
    Contains unit tests for the custom_map function.
    """
    def test_1(self):
        """
        Test if the custom_map function can return the square root of each element in the array.
        """
        test_arr = [4, 9, 16, 25]
        self.assertEqual(custom_map(test_arr, math.sqrt), [2, 3, 4, 5])
    
    def test_2(self):
        """
        Test if the custom_map function convert an array of string to lower cases and return them.
        """
        str = ["HEllo", "worlD", "UNIT", "teSTING"]
        self.assertEqual(custom_map(str, to_lower), ["hello", "world", "unit", "testing"])



if __name__ == '__main__':
    unittest.main()
