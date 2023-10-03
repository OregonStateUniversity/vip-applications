import unittest

# Define the custom map function
def custom_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result

# Define a function that squares a number
def square(x):
    return x ** 2

class TestCustomMapFunction(unittest.TestCase):

    def test_square_function(self):
        # Test if the custom_map() function correctly applies the square function
        numbers = [1, 2, 3, 4, 5]
        result = custom_map(square, numbers)
        self.assertEqual(result, [1, 4, 9, 16, 25])

    def test_empty_iterable(self):
        # Test if the custom_map() function works with an empty iterable
        empty_list = []
        result = custom_map(square, empty_list)
        self.assertEqual(result, [])

    def test_string_length_function(self):
        # Test if the custom_map() function correctly applies a string length function
        strings = ["apple", "banana", "cherry"]
        result = custom_map(len, strings)
        self.assertEqual(result, [5, 6, 6])

if __name__ == '__main__':
    unittest.main()
