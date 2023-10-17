from application import map_function
import unittest

class TestMapFunction(unittest.TestCase):
    """test class for map_function"""
    def test1(self):
        list1 = [2, 4, 6]
        answer = map_function([1, 2, 3])
        self.assertEqual(list1, answer)


if __name__ == '__main__':
    unittest.main(verbosity=2)
