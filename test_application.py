import unittest
from application import map_func


class TestMapFunction(unittest.TestCase):

    def test_map_function(self):
        input_list = [1, 2, 3]
        expected = [2, 4, 6]
        result = map_func(lambda x: x * 2, input_list)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
