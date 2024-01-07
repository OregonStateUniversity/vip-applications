def map(iterable, map_func) -> array:
    """
    Takes an iterable data structure and function as paramaters and applies the function to all objects
    in the iterable. Returns a new array with the resulting outputs.

    :param iterable:    an iterable object to be altered by the map function
    :param map_func:    the function to call on each element of the iterable
    :return:            a new array whose elements are the altered objects from the original iterable
    """

    mapped_array = []

    #iterate over original object, apply map_func to each and append outputs to mapped_array
    for object in iterable:
        mapped_array.append(map_func(object))
        
    return mapped_array
