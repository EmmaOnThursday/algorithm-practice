"""input: missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
output: 8"""

def missing_number(nums_list, max_num):
    """Given a number, determine what number is missing from its range in nums_list."""
    # runtime = O(n)
    # runspace = O(n)

    correct_range = range(1, max_num+1)
    missing = sum(correct_range) - sum(nums_list)
    return missing

print missing_number([2, 1, 4, 3, 6, 5, 8, 10, 9], 10)


def missing_number2(nums_list, max_num):
    """Given a number, determine what number is missing from its range in nums_list."""
    # runtime = O(n log n)
    # runspace = O(1)

    nums_list.sort()
    prev = 0
    for i in nums_list:
        if i != prev + 1:
            return prev + 1
        prev += 1

print missing_number2([2, 1, 4, 3, 6, 5, 8, 10, 9], 10)



def missing_number3(nums_list, max_num):
    """Given a number, determine what number is missing from its range in nums_list."""
    # runtime = O(n^2)
    # requires no additional space

    for item in nums_list:
        if ((max_num+1) - item) not in nums_list:
            return ((max_num+1) - item)

print missing_number3([2, 1, 4, 3, 6, 5, 8, 10, 9], 10)

def missing_number4(nums_list, max_num):
    """Given a number, determine what number is missing from its range in nums_list."""
    # runtime = O(n)
    # requires no additional space

    missing = sum(range(1, max_num+1)) - sum(nums_list)
    return missing

print missing_number4([2, 1, 4, 3, 6, 5, 8, 10, 9], 10)



# Most simple; has runtime O(n^2), runspace O(1)
# for i in range(1, max_num+1):
#     if i not in nums_list:
#         return 1



