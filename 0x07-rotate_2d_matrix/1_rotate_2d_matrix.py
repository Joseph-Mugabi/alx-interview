#!/usr/bin/python3
"""
rotate 2D matrix
"""


def rotate_2d_matrix(matrix):
    n = len(matrix)
    rotated_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # rotate values
            rotated_matrix[j][n - i - 1] = matrix[i][j]

    for i in range(n):
        # update the original matrix in-place
        matrix[i] = rotated_matrix[i]

if __name__ == '__main__':
    mylist1 = [
         [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rotate_2d_matrix(mylist1)
    print(mylist1)
