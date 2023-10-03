"""map function"""""
def map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result
