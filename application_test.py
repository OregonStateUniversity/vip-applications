import unittest
from application import map_func


class TestMap(unittest.TestCase):

    def test_map_func_with_double_function(self):
        '''
        Tests the map_func with a function that doubles the values
        '''

        def double(x):
            return x * x

        input = [2, 4, 6, 8]
        expected_output = [4, 16, 36, 64]

        result = map_func(double, input)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
