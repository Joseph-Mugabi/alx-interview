#!/usr/bin/python3
"""returns a list of lists of integers representing
the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """Initialize the triangle with the first row """
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        triangle = pascal_triangle(n - 1)
        p_row = triangle[-1]
        c_row = [1]
        for i in range(len(p_row) - 1):
            c_row.append(p_row[i] + p_row[i + 1])
        c_row.append(1)
        triangle.append(c_row)
        return triangle
