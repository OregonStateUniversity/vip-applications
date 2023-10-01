def map(f, arr):
    """map function"""
    output = []
    for i in arr:
        output.append(f(i))
    return output


def add(n):
    """function adds one to an item"""
    return n + 1
