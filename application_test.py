import unittest
from application import add_ten

class Test_add_ten_function(unittest.TestCase):
    def test_integers(self):
        numbers = [0, 5, 20, 62, 500]
        self.assertEqual(list(map(add_ten, numbers)), [10, 15, 30, 72, 510])


if __name__ == "__main__":
    unittest.main()