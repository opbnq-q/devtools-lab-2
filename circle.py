import math


def area(r):
    """calculates the area of a circle.

    args:
        r: the radius of the circle. (float)

    returns:
        the area of the circle. (float)

    example:
        area(2) = 12.566370614359172
    """
    return math.pi * r * r


def perimeter(r):
    """calculates the perimeter of a circle.

    args:
        r: the radius of the circle. (float)

    returns:
        the perimeter of the circle. (float)

    example:
        perimeter(2) = 12.566370614359172
    """
    return 2 * math.pi * r
