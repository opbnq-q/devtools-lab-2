def area(a, h):
    """calculates the area of a triangle.

    args:
        a: the base of the triangle. (float)
        h: the height of the triangle. (float)

    returns:
        the area of the triangle. (float)

    example:
        area(4, 3) = 6
    """
    return a * h / 2


def perimeter(a, b, c):
    """calculates the perimeter of a triangle.

    args:
        a: the first side of the triangle. (float)
        b: the second side of the triangle. (float)
        c: the third side of the triangle. (float)

    returns:
        the perimeter of the triangle. (float)

    example:
        perimeter(3, 4, 5) = 12
    """
    return a + b + c