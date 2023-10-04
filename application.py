# Daniel Grossberg
# grossbed@oregonstate.edu
# Application for Vertically Integrated Projects program at Oregon State University

from typing import Callable, Iterable

def custom_map(func: Callable, iter: Iterable) -> list:
    """Custom map function implementation """
    mapped_iter = [func(i) for i in iter]
    return mapped_iter

