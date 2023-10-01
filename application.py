def custom_map(arr, custom_function):
    '''
    Function definition that takes an array and 
    a customFunction as two parameters. 
    Returns a new array which is the result of 
    applying the customFunction to each element 
    of the original array (i.e., arr). 
    '''
    new_arr = []
    for each in arr:
        new_arr.append(custom_function(each))
    return new_arr

def to_lower(str):
    return str.lower()