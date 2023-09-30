
def custom_map(arr, func) -> list:
    """
    Custom mapping function that will take any array and a given function, and 
    apply that function to every item in the array. Uses dictionary comprehension 
    to generate this new array. 
    """
    new_arr = [func(x) for x in arr]
    return new_arr