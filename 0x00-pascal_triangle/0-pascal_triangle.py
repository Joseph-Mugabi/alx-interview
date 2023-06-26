#!/usr/bin/python3
"""
returns a list of lists of integers representing
the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n.
    Initialize the triangle with the first row"""
    triangle = [[1]]

    # Generate the next row of the triangle n times
    for i in range(1, n):
        # Initialize with the 1st element
        row = [1]
        for j in range(1, i):
            # calcu the nxt element as the sum of the two elemnts above it
            nxt_elemnt = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(nxt_elemnt)
        row.append(1)  # add the last element
        triangle.append(row)

    return triangle
