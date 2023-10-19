import unittest
from application import my_map_func


class TestApplication(unittest.TestCase):
    """Contains a test for application.py."""
    def test_1(self):
        """Tests my map function."""
        array_1 = [0, 1, 2, 5, 12, 100, -1, -100]
        result = my_map_func(array_1)
        self.assertEqual(result, [0, 1, 4, 25, 144, 10000, 1, 10000])


if __name__ == "__main__":
    unittest.main()