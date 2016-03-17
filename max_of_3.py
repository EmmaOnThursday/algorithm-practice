def max_of_three(num1, num2, num3):
    """Returns the largest of three integers"""

    if num1 >= num2:
        if num1 > num3:
            return num1
        else:
            return num3
    elif num2 >= num1:
        if num2 > num3:
            return num2
        else:
            return num3



# TESTS
print max_of_three(1,2,3)
print 3

print max_of_three(6,4,17)
print 17

print max_of_three(1,1,6)
print 6

print max_of_three(5,5,4)
print 5

print max_of_three(1,1,1)