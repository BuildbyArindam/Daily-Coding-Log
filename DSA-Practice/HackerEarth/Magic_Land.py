"""
Problem   : Magic Land
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/magic-land-18/
Date      : 2026-08-22
Difficulty: Easy
Topics    : Data Structures, Implementation

Approach:
For each test case, compute the longest run of equal consecutive
elements along each row (max_mr) and along each column (max_mc)
independently, using a simple linear scan with a running counter
that resets on value change. The answer is max_mr * max_mc, since
the largest "uniform rectangle-like" magic value is bounded by the
best row-run combined with the best column-run.

Time Complexity : O(n * m) per test case (single pass over rows,
                   single pass over columns)
Space Complexity: O(n * m) to store the grid
"""


# ------------------------ Solution ----------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    idx = 0
    t = int(input_data[idx])
    idx += 1
    for _ in range(t):
        n = int(input_data[idx])
        m = int(input_data[idx + 1])
        idx += 2
        grid = []
        for _ in range(n):
            grid.append([int(x) for x in input_data[idx : idx + m]])
            idx += m
        max_mr = 0
        for i in range(n):
            curr_max = 1
            count = 1
            for j in range(1, m):
                if grid[i][j] == grid[i][j - 1]:
                    count += 1
                else:
                    curr_max = max(curr_max, count)
                    count = 1
            curr_max = max(curr_max, count)
            max_mr = max(max_mr, curr_max)
        max_mc = 0
        for j in range(m):
            curr_max = 1
            count = 1
            for i in range(1, n):
                if grid[i][j] == grid[i - 1][j]:
                    count += 1
                else:
                    curr_max = max(curr_max, count)
                    count = 1
            curr_max = max(curr_max, count)
            max_mc = max(max_mc, curr_max)
        print(max_mr * max_mc)

if __name__ == "__main__":
    solve()
