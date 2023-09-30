import unittest
from application import n_squared, simple_map


class TestSimpleMap(unittest.TestCase):
    """
    Is some unit tests that will test my implemented map 
    function against pythons built in map function
    """

    def test_simple_map_n_squared(self):
        """
        Test of pythons map function against created map 
        function using n_squared function
        """
        test_array = [2, 3, -100, 100, 0, 123, 43]
        expected = list(map(n_squared, test_array))  # Convert map obj to list
        result = simple_map(n_squared, test_array)
        self.assertListEqual(expected, result)

    def test_simple_map_edge_case(self):
        """
        Edge case test of map function to test an empty array
        """
        test_array = []
        expected = list(map(n_squared, test_array))  # Convert map obj to list
        result = simple_map(n_squared, test_array)
        self.assertListEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
