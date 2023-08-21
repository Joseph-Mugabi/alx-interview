#!/usr/bin/python3
"""
rotate 2D matrix
"""

def rotate_2d_matrix(matrix):
    """2D matrix, rotate it 90 degrees clockwise"""
    for j in range(len(matrix)):
        for i in range(j + 1, len(matrix)):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    for j in range(len(matrix)):
        lw, hgh = 0, len(matrix[j]) - 1
        while (lw < hgh):
            matrix[j][lw], matrix[j][hgh] = matrix[j][hgh], matrix[j][lw]
            lw += 1
            hgh -= 1
