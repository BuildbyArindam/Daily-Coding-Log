"""
Problem: Valid Sudoku (Sudoku Solver variant)
Link: https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118522/offering/1380919
Platform: Code360
Date Solved: 2026-09-15
Difficulty: Medium
Topic: Backtracking, Matrix/2D Array, Constraint Satisfaction

Approach:
Backtracking. Scan for the first empty cell (value 0); try digits 1-9 in order.
For each candidate digit, check the row, column, and 3x3 sub-box for conflicts
before placing it. Recurse into the next empty cell; if no digit works, undo
(backtrack) and try the next candidate. Board is filled in place.

Time Complexity: O(9^m) worst case, where m = number of empty cells
                  (bounded in practice by constraint propagation from the checks)
Space Complexity: O(1) extra (in-place mutation) + O(m) recursion stack depth
"""


# ------------------------------ Solution ----------------------------------------


def isItSudoku(matrix):
    def solve():
        for row in range(9):
            for col in range(9):
                if matrix[row][col] == 0:
                    for num in range(1, 10):
                        if num in matrix[row]:
                            continue
                        valid = True
                        for r in range(9):
                            if matrix[r][col] == num:
                                valid = False
                                break
                        if not valid:
                            continue
                        start_row = (row // 3) * 3
                        start_col = (col // 3) * 3
                        for r in range(start_row, start_row + 3):
                            for c in range(start_col, start_col + 3):
                                if matrix[r][c] == num:
                                    valid = False
                                    break
                            if not valid:
                                break
                        if not valid:
                            continue
                        matrix[row][col] = num
                        if solve():
                            return True
                        matrix[row][col] = 0
                    return False
        return True
    return solve()
