def map_function(input_list):
    """map function which multiples each number in array by 2
    :parameter input_list: an array of integers
    :returns: the modified array"""
    for i in range(len(input_list)):
        input_list[i] *= 2

    return input_list


