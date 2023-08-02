#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    # Check if a queen can be placed at board[row][col]
    # without conflicting with any other queens

    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_n_queens_util(board, col, N, solutions):
    # Base case: If all queens are placed
    if col == N:
        solution = []
        for i in range(N):
            row = ''
            for j in range(N):
                if board[i][j] == 1:
                    row += 'Q'
                else:
                    row += '.'
            solution.append(row)
        solutions.append(solution)
        return

    # Consider this column and try placing a queen in all rows
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place the queen
            board[i][col] = 1

            # Recur to place the rest of the queens
            solve_n_queens_util(board, col + 1, N, solutions)

            # If placing queen in board[i][col] doesn't lead to a solution
            # then remove the queen from board[i][col]
            board[i][col] = 0

def solve_n_queens(N):
    # Create an NxN chessboard filled with zeros
    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)

    # Print the solutions
    for solution in solutions:
        for row in solution:
            print(row)
        print()

if __name__ == '__main__':
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_n_queens(N)
