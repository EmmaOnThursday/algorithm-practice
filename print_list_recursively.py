# Printing a list recursively

# Base case: empty list
# OR
# on last item in the list

def print_list_recursively(nums):
    if nums == []:
        return
    else:
        print nums.pop(0)
        return print_list_recursively(nums)



