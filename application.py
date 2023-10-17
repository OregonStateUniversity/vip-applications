def map_func(func, input):
  result = []
  for elm in input:
    result.append(func(elm))
  return result
