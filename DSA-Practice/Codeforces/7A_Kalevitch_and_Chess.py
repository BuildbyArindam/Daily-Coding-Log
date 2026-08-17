"""
Problem: Kalevitch and Chess
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/7/A
Date Solved: 2026-08-17
Difficulty: *1100
Topics: Brute Force, Constructive Algorithms

Approach:
Read the 8x8 board. Count how many rows are fully black ("BBBBBBBB").
If all 8 rows are black, the minimum paint operations is just 8
(painting all rows OR all columns achieves this — no need to double count).
Otherwise, count fully-black columns separately and add that to the
fully-black row count, since rows and columns are independent paint ops.

Time Complexity:  O(1) — board is fixed at 8x8 (64 cells), so all loops are bounded constants.
Space Complexity: O(1) — only the 8x8 board is stored, no extra scaling structures.
"""


# ------------------------ Solution ------------------------


import sys

def solve():
    board = [sys.stdin.readline().strip() for _ in range(8)]
    black_rows = sum(1 for row in board if row == "BBBBBBBB")
    if black_rows == 8:
        print(8)
        return
    black_cols = 0
    for col in range(8):
        if all(board[row][col] == "B" for row in range(8)):
            black_cols += 1
    print(black_rows + black_cols)

if __name__ == "__main__":
    solve()
