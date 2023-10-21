def map_func(func, list):
    '''
    A map function that takes in a function (func) and a list and 
    returns a list (results) with the return values of the func on the list
    '''

    results = []

    for item in list:
        results.append(func(item))
    return results
