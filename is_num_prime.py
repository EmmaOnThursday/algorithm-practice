def is_prime(num):
    """Is a num a prime number?"""

    if num in [0, 1]:
        return False

    for x in range(2, (num-1)):
        if num % x == 0:
            return False

    return True
