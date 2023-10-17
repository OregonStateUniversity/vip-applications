import unittest
from application import mapfunction


class MyTestCase(unittest.TestCase):
    def test_mapfunction(self):
        map_result = mapfunction(5, 9)
        self.assertEqual(map_result, 14)  # add assertion here


if __name__ == '__main__':
    unittest.main()
