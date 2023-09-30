from application import custom_map

def test_custom_map1():
    """
    Tests and checks whether squaring numbers in the array is accurate.
    """
    numbers = [1, 3, 5]
    squared_nums = custom_map(numbers, lambda x: x*x)

    assert squared_nums == [1, 9, 25]

def test_custom_map2():
    """
    Tests and checks whether shifting letters by 1 is accurate.
    """
    letters = ["a", "e", "g"]

    shifted_lets = custom_map(letters, lambda x: chr(ord(x)+1))

    assert shifted_lets == ["b", "f", "h"]

if __name__ == '__main__':
    test_custom_map1()
    test_custom_map2()
    print("Tests passed!")