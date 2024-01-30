import unittest
from application import map_func


class TestMapFunction(unittest.TestCase):

    def test_map_function(self):
        input_list = [4, 7, 18]
        expected = [8, 14, 36]
        result = map_func(lambda x: x * 2, input_list)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
