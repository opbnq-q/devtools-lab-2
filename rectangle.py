def area(a, b):
    """calculates the area of a rectangle.

    args:
        a: the length of the rectangle. (float)
        b: the width of the rectangle. (float)

    returns:
        the area of the rectangle. (float)

    example:
        area(2, 3) = 6
    """
    return a * b


def perimeter(a, b):
    """calculates the perimeter of a rectangle.

    args:
        a: the length of the rectangle. (float)
        b: the width of the rectangle. (float)

    returns:
        the perimeter of the rectangle. (float)

    example:
        perimeter(2, 3) = 10
    """
    return 2 * (a + b)