def custom_map(function, iter_list):
    """
    Custom map function that takes two parameters; a list of iterables
    and a given function. It applies each item of the list to the
    given function and returns the results in a different list.
    """

    result = []
    for item in iter_list:
        result.append(function(item))
    return result


def odd_or_even(num):
    """
    Takes an integer as a parameter and returns whether it's "ODD" or "EVEN".
    """

    if (num % 2) == 0:
        return "EVEN"
    return "ODD"