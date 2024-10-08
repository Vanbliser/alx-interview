#!/usr/bin/python3


"""Contains def pascal_triangle(n) function"""


def pascal_triangle(n):
    """a funtion that returns a list of lists of integers representing
    the Pascal’s triangle of n.

    Args:
        n (int): you can assume n will be an integer

    Returns:
        list: a list of list of integers representing the Pascal’s 
              triangle of n.
    """

    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1,1]]
    else:
        triangle = pascal_triangle(n-1)
        previous_row = triangle[-1]
        next_row = [1]
        for i in range(1, n-1):
            next_row.append(previous_row[i] + previous_row[i-1])
        next_row.append(1)
        triangle.append(next_row)
    return triangle
