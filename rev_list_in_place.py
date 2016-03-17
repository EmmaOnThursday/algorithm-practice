def rev_list_in_place(lst):
    """Reverse list in place.

    You cannot do this with reversed(), .reverse(), or list slice assignment!
    input = [1,2,3,4]
    output = [4,3,2,1]
    """
    for i in range(len(lst)-1, -1, -1):
        lst.append(lst[i])
    
    half = len(lst)/2
    lst = lst[half:]
    return lst

lst = [1,2,3,4]
print lst
print rev_list_in_place(lst)

