"""
Name: Keshavan Sridhar
OSU Email: sridhake@oregonstate.edu
Date: 9/30/23
Description: Custom map function for Vertically Integrated Projects Program

"""

# import typing library for type hints
from typing import Callable, Generator, Sequence


def map(function: Callable, *iterable: Sequence) -> Generator:
    """
    The map function takes a function and iterable values as inputs, and applies the function to each value of the
    inputs. The total number of function calls will be equivalent to the number of elements in the smallest
    inputted iterable value.

    :param Callable function: the input function that values are applied to
    :param Sequence iterable: the input iterable(s) value(s)
    :return Generator: the output of applying the input function to each value of the input iterables
    """
    # list with each iterable in order of input
    inputs = list(iterable)

    # check if first input is actually iterable. Raises TypeError if not iterable
    iter(inputs[0])

    # find number of iterations (minimum length amongst all iterables)
    min_length = len(inputs[0])
    for i in inputs:
        # check if input is actually iterable. Raises TypeError if not iterable
        iter(i)

        # if any iterable is empty, exit loop
        if min_length == 0:
            break
        length = len(i)
        if min_length > length:
            min_length = length

    # in min_length iterations, get function outputs for all inputted iterables
    output_list = []
    temp_list = []
    for index in range(min_length):
        for val in inputs:
            temp_list.append(val[index])
        output_list.append(function(*temp_list))
        temp_list = []

    # return a generator object for the map
    return (i for i in output_list)
