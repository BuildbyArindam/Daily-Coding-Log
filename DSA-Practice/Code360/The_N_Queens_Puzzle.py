"""
Problem   : The N-Queens Puzzle
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118522/offering/1380923
Difficulty: Medium
Topic     : Backtracking, Recursion, Constraint Satisfaction
Date      : 2026-09-17

Approach:
    Place queens row by row. For each row, try every column and check if
    it's safe using three hash sets: `cols` (column already occupied),
    `diag1` (row - col, constant along a "\" diagonal), and
    `diag2` (row + col, constant along a "/" diagonal). If safe, place
    the queen, recurse to the next row, then backtrack by removing the
    queen and clearing its entries from the sets. When row == n, a full
    valid board has been found — flatten it and store it.

Time complexity : O(N!) — worst case branching factor shrinks each row,
                   but backtracking still explores factorially many
                   partial placements before pruning.
Space complexity : O(N^2) for the board + O(N) for the recursion stack
     


# ---------------------------------- Solution ---------------------------------------


from os import *
from sys import *
from collections import *
from math import *

def nQueens(n):
    ans = []
    board = [[0] * n for _ in range(n)]
    cols = set()
    diag1 = set() 
    diag2 = set() 
    def solve(row):
        if row == n:
            current = []
            for r in range(n):
                current.extend(board[r])
            ans.append(current)
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            board[row][col] = 1
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            solve(row + 1)
            board[row][col] = 0
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
    solve(0)
    return ans
