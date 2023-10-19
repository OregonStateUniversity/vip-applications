def my_map_func(arr):
    """Squares each element in an array, and returns the new mapped array."""
    map_arr = [0] * len(arr)
    for i in range(len(arr)):
        map_arr[i] = arr[i] * arr[i]

    return map_arr

