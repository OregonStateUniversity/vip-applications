def custom_map(func, iterable):
    """
    Custom map function that feeds the iterable into the function and returns the result

    :param func: Represents a function to be applied to each item in the iterable
    :param iterable: Represents a collection of items to be iterated over

    :return result: Represents the result of the function applied to each item in the iterable
    """
    result = []
    for item in iterable:
        result.append(func(item))
    return result

