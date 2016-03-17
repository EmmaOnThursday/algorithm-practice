"""Define a function that takes in a decimal number and converts it to hexadecimal.
    Print the hexadecimal at the end of the function.
    Your inputs will all be postive integers; no need to validate."""



def convert_low_numbers(num):
    """Take in a positive integer; return hexadecimal equivalent.

    >>> decimal_to_hexadecimal(16)
    10

    >>> decimal_to_hexadecimal(21335)
    5357

    >>> decimal_to_hexadecimal(114976002)
    6DA6502
    
    """

    convert_to = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E',15:'F'}

    if num in range(10):
        return str(num)
    elif num in range(10,16):
        return convert_to[num]
    else:
        # raise Exception
        return "ERROR"


def decimal_to_hexadecimal(dec, hexadecimal=""):
    """ """
    hexadecimal = convert_low_numbers(dec % 16) + hexadecimal
    mult = dec / 16

    if mult < 16:
        hexadecimal = convert_low_numbers(mult) + hexadecimal
        print hexadecimal
    else:
        decimal_to_hexadecimal(mult, hexadecimal)








