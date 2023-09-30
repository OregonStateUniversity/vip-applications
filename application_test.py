import unittest
from application import custom_map


class TestCustomMap(unittest.TestCase):
    """
    Test the custom_map function using lambda functions and lists as the iterables
    """
    def test_custom_map__square_func(self):
        """
        Test that the custom_map function returns the expected result for a squared function
        """
        self.assertEqual(custom_map(lambda x: x ** 2, [1, 2, 3]), [1, 4, 9])

    def test_custom_map__cube_func(self):
        """
        Test that the custom_map function returns the expected result for a cubed function
        """
        self.assertEqual(custom_map(lambda x: x ** 3, [1, 2, 3]), [1, 8, 27])

    def test_custom_map__empty_iterable(self):
        """
        Test that the custom_map function returns the expected result for an empty iterable
        """
        self.assertEqual(custom_map(lambda x: x ** 3, []), [])


if __name__ == '__main__':
    unittest.main()