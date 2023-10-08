import unittest
import application

def multiply_by_ten(number):
  """Multiplies a given number by 10"""
  return number * 10

def add_exclamation(str):
  """Adds three exclamation points to a given string"""
  return str + '!!!'

class TestMyMap(unittest.TestCase):
  """Unit tests testing the functionality of the custom map function"""
  def test_map_multiply(self):
    """Tests the my_map function against python's built in map function using the multiply by ten function defined above"""
    num_list = [10, -10, 5, 2, 30]
    mapped_list = list(map(multiply_by_ten, num_list))
    my_mapped_list = application.my_map(multiply_by_ten, num_list)
    self.assertListEqual(mapped_list, my_mapped_list)

  def test_map_add_exclamations(self):
    """Tests the my_map function against python's built in map function using the add exclamations function defined above"""
    word_list = ['Hey', 'you', 'guys']
    mapped_list = list(map(add_exclamation, word_list))
    my_mapped_list = application.my_map(add_exclamation, word_list)
    self.assertListEqual(mapped_list, my_mapped_list)

if __name__ == '__main__':
  unittest.main()