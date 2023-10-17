def mapfunction(item1, item2):
    """
    a map function for the application
    """
    return item1 + item2
group1 = ("item1", "item2", "item3")
group2 = ("item4", "item5", "item6")
map_result = map(mapfunction, group1, group2)

print(list(map_result))

