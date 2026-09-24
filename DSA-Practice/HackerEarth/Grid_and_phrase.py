"""
Problem   : Grid and phrase
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/practice-problems/algorithm/jadvaliioo-62280ff6/
Difficulty: Easy
Topics    : Arrays, Brute-force search, Data Structures, Multi-dimensional
Date      : 2026-09-24

Approach:
    Brute force over the grid. For every valid starting cell, build the
    4-letter string in each of four directions (horizontal, vertical,
    down-right diagonal, up-right diagonal) and compare it with "saba".
    Loop bounds are limited so the 4-cell window never leaves the grid.

Complexity:
    Time  : O(n * m). Four passes over the grid, each doing constant work
            (a 4-character comparison) per cell.
    Space : O(n * m) for the stored grid, O(1) extra.
"""


# ---------------------------------------- Solution ---------------------------------------------


n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]
word = "saba"
count = 0
for i in range(n):
    for j in range(m - 3):
        if (grid[i][j] +
            grid[i][j + 1] +
            grid[i][j + 2] +
            grid[i][j + 3]) == word:
            count += 1
for i in range(n - 3):
    for j in range(m):
        if (grid[i][j] +
            grid[i + 1][j] +
            grid[i + 2][j] +
            grid[i + 3][j]) == word:
            count += 1
for i in range(n - 3):
    for j in range(m - 3):
        if (grid[i][j] +
            grid[i + 1][j + 1] +
            grid[i + 2][j + 2] +
            grid[i + 3][j + 3]) == word:
            count += 1
for i in range(3, n):
    for j in range(m - 3):
        if (grid[i][j] +
            grid[i - 1][j + 1] +
            grid[i - 2][j + 2] +
            grid[i - 3][j + 3]) == word:
            count += 1
print(count)
