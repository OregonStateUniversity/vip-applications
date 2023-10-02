import unittest
from application import custom_map, odd_or_even


class TestCase(unittest.TestCase):
  
    def test_1(self):
        
        test_list = [0, 2, 10]
        expected = ["EVEN", "EVEN", "EVEN"]
        result = custom_map(odd_or_even, test_list)
        self.assertEqual(result, expected)
    
    def test_2(self):
        
        test_list = [1, 5, 11]
        expected = ["ODD", "ODD", "ODD"]
        result = custom_map(odd_or_even, test_list)
        self.assertEqual(result, expected)

    def test_3(self):
        
        test_list = [15, 206, -15]
        expected = ["ODD", "EVEN", "ODD"]
        result = custom_map(odd_or_even, test_list)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()