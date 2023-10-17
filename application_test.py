import unittest
from application import *

class TestMap(unittest.TestCase):

    def test_square_function(self):
        numbers = [1, 2, 3, 4, 5]
        squared_numbers = custom_map(square, numbers)
        self.assertEqual(squared_numbers, [1, 4, 9, 16, 25])

def square(x):
    return x ** 2

if __name__ == '__main__':
    unittest.main()
