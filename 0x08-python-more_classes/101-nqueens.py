#!/usr/bin/python3
"""N queens puzzle"""

import sys


def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def nqueens_util(board, row, N, solutions):
    if row == N:
        solution = ["." * col + "Q" + "." * (N - col - 1) for col in board]
        solutions.append(solution)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            nqueens_util(board, row + 1, N, solutions)
            board[row][col] = 0


def nqueens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    nqueens_util(board, 0, N, solutions)

    for solution in solutions:
        for row in solution:
            print(row)
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
