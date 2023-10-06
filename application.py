# Daniel Grossberg
# grossbed@oregonstate.edu
# Application for Vertically Integrated Projects program at Oregon State University

from typing import Callable


def custom_map(func: Callable, iter: list) -> list:
    """
    Custom map function implementation: applies the func to each element in the iter list.
    :param: func: a callable function
    :param: iter: an iterable list object
    :return: a new list containing all elements in the iter list after the func is applied
    to each element.
    """
    return [func(i) for i in iter]

