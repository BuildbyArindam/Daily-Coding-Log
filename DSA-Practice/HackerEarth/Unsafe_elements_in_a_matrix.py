"""
Problem   : Unsafe Elements in a Matrix
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/practice-problems/algorithm/kshitiz-and-matrix-7ddc9719/
Difficulty: Medium
Topics    : Arrays, Data Structures, Multi-dimensional
Date      : 2026-09-24

Approach:
    Find the global minimum and maximum of the matrix. Any row or column
    containing either value is unsafe, so mark those rows and columns in
    a single pass. The safe cells are the intersection of safe rows and
    safe columns: (N - unsafe_rows) * (M - unsafe_cols).

Complexity:
    Time  : O(N * M) per test case (read, then scan the matrix once)
    Space : O(N * M) for the stored matrix, plus O(N + M) for the flags
"""


# ---------------------------------------- Solution ------------------------------------------


import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    matrix = []
    mn = float('inf')
    mx = float('-inf')
    for i in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)
        row_min = min(row)
        row_max = max(row)
        mn = min(mn, row_min)
        mx = max(mx, row_max)
    bad_rows = [False] * N
    bad_cols = [False] * M
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == mn or matrix[i][j] == mx:
                bad_rows[i] = True
                bad_cols[j] = True
    safe_rows = N - sum(bad_rows)
    safe_cols = M - sum(bad_cols)
    answer = safe_rows * safe_cols
    print(answer)
