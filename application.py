def simple_map(func, iterable):
    """Simple defined map function, missing features of Pythons built in map"""
    mapped_array = []
    for item in iterable:
        value = func(item)
        mapped_array.append(value)
    return mapped_array


def n_squared(n):
    """Takes int n and squares it"""
    return n**2