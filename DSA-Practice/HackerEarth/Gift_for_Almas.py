"""
Problem : Gift for Almas
Platform: HackerEarth
Link    : https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/practice-problems/algorithm/gift-for-almas-3-33d2f7c7/
Date    : 2026-09-24
Difficulty: Easy
Topics  : Arrays, Data Structures, Multi-dimensional

Approach:
    Apply each instruction to the N x N matrix in order, rotating it
    90 degrees per move. 'R' is clockwise (reverse rows, then transpose
    via zip). 'L' is counterclockwise (transpose, then reverse rows).
    Print the final matrix.

Complexity:
    Time : O(K * N^2), where K = len(instructions); each rotation rebuilds the matrix
    Space: O(N^2) for the rotated copy
"""


# ------------------------------------ Solution -----------------------------------------------------


n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
instructions = input().strip()
for move in instructions:
    if move == 'R':
        matrix = [list(row) for row in zip(*matrix[::-1])]
    elif move == 'L':
        matrix = [list(row) for row in zip(*matrix)][::-1]
for row in matrix:
    print(*row)
