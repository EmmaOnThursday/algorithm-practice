def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place."""
    # turn into a string
    s = str(num)
    for i in s[::-1]:
        print i

# print_digits(123456)


def print_digits2(n):
    """Given int, print digits in reverse order, starting with the ones place."""
    # using math

    i = 1
    while n % i != n:
        i = i * 10

    digits = []
    while i > 0:
        digits.append(n/i)
        print i, n, n/i
        n =  n % i
        i = i/10
   
    for digit in digits[:0:-1]:
        print digit
    print len(digits[:0:-1])

print_digits2(8393008735)
