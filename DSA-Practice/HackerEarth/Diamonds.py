"""
Problem: Diamonds
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/diamonds-4/
Difficulty: Easy
Topics: Implementation, Ad-hoc, Basic Programming
Date: 2026-08-27

Approach:
Read an N x M grid of characters for each test case. A "diamond" is
formed by a 2x2 block shaped like:
    / \
    \ /
i.e. grid[r][c]='/', grid[r][c+1]='\', grid[r+1][c]='\', grid[r+1][c+1]='/'.
Slide a 2x2 window over every possible top-left corner (r, c) and count
matches.

Time Complexity: O(N*M) per test case — single pass over all 2x2 windows
Space Complexity: O(N*M) to store the grid
"""


# -------------------------- Solution ------------------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    for _ in range(t):
        n = int(input_data[idx])
        m = int(input_data[idx + 1])
        idx += 2
        grid = []
        for _ in range(n):
            grid.append(input_data[idx:idx + m])
            idx += m
        count = 0
        for r in range(n - 1):
            for c in range(m - 1):
                if (grid[r][c] == '/' and
                    grid[r][c + 1] == '\\' and
                    grid[r + 1][c] == '\\' and
                    grid[r + 1][c + 1] == '/'):
                    count += 1
        print(count)

if __name__ == "__main__":
    solve()
