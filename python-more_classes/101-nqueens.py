#!/usr/bin/python3
"""Solves the N queens puzzle with backtracking.

Usage: nqueens N

Prints every arrangement of N non-attacking queens on an N x N board,
one solution per line, as a list of [row, column] pairs.
"""
import sys


def is_safe(board, row, col):
    """Check whether a queen can be placed at (row, col).

    Args:
        board: list where board[r] is the column of the queen on row r.
        row: the row being filled.
        col: the candidate column.

    Returns:
        True if no already placed queen attacks that square.
    """
    for previous in range(row):
        if board[previous] == col:
            return False
        if abs(board[previous] - col) == abs(previous - row):
            return False
    return True


def solve(board, row, size):
    """Place queens row by row, printing each complete solution.

    Args:
        board: list holding the column chosen for each filled row.
        row: the row to fill next.
        size: the size of the board.
    """
    if row == size:
        print([[index, board[index]] for index in range(size)])
        return
    for col in range(size):
        if is_safe(board, row, col):
            board[row] = col
            solve(board, row + 1, size)


def main():
    """Validate the command line argument and run the solver."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if size < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve([0] * size, 0, size)


if __name__ == "__main__":
    main()
