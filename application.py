# Author:           Taylor Jordan
# GitHub username:  RangerTJ
# Date:             1/6/2024
# Description:      Application map function for the OSU VIP program for CS online post-bacc students.


def map(array, func):
    """
    Iterates through all elements of an array and maps and maps the results of applying a function
    to the original value to a new array.

    Receives an array of numerical elements and a function that returns a numerical result of being applied to
    a numerical argument.

    Returns the new array of mapped/modified values.
    """
    mapped_array = []
    for num in range(len(array)):
        mapped_array.append(func(array[num]))
    return mapped_array


# Testing
# def plus_one(original_number):
#     """
#     Receives a number as an argument and increases it by +1.
#     Returns the new result.
#     """
#     return original_number + 1
#
# test_arr = [1, 2, 3, 4, 5]
# print(map(test_arr, plus_one))
