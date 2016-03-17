def concat_lists(list1, list2):
    """Combine lists."""

    for item in list2:
        list1.append(item)
    return list1

list1 = [2,3,4]
list2 = ['frog', 'prince', 'kiss']

list3 = []

print concat_lists(list1, list2)
print concat_lists(list2, list3)