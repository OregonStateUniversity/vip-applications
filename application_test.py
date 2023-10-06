from application import *

def test_custom_map_with_ints():
    """Test integer inputs for custom map"""
    # test squares happy path
    assert custom_map(lambda x: x**2, [-3, -2, -1, 0, 1, 2, 3]) == [9, 4, 1, 0, 1, 4, 9]
    # test squares large ints
    assert custom_map(lambda x: x**2, [-987, 1342]) == [974169, 1800964]
    # test odd or even
    assert custom_map(lambda x: x % 2 == 0, [0, 1, 2, 3, 4, 5]) == [True, False, True, False, True, False]


def test_custom_map_with_strs():
    """Test str inputs for custom map"""
    # test str happy path
    assert custom_map(lambda x: x[1:-1], ["abc", "aabbcc", "aaabbbccc"]) == ["b", "abbc", "aabbbcc"]
    # test str slice from specific index
    assert custom_map(lambda x: x[x.index("b"):x.index("c")], ["abc", "aabbcc", "aaabbbccc"]) == ["b", "bb", "bbb"]
    # test replace spaces
    assert custom_map(lambda x: x.replace((" "), ("")), ["a b c", "a a b b c c", "a a a b b b c c c"]) == ["abc", "aabbcc", "aaabbbccc"]

