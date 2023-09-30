
def custom_map(arr, func):
    new_arr = [func(x) for x in arr]
    return new_arr