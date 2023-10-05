from typing import List


def map(arr: List[int]) -> List[int]:
    """
    Takes a List and doubles every value
    Args:
        arr (List[int]): a List of integers

    Returns:
        new_arr (List[int]): a different List of integers with the integers doubled from the original List
    """
    new_arr = []
    for i, value in enumerate(arr):
        new_arr.append(value * 2)

    return new_arr
