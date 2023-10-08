def my_map(func, arr):
  """A custom map function that mimics Python's built-in map function"
  new_arr = []
  for item in arr:
    new_item = funct(item)
    new_arr.append(new_item)
  return new_arr
