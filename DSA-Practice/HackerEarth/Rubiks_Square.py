"""
Problem: Rubik's Square
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/rubiks-square-2/
Date: 2026-08-24
Difficulty: Medium
Topic: Implementation / Matrix Simulation

Approach:
Read an N x N matrix, then apply R row-rotation queries and C column-rotation
queries (each query rotates the specified row/column left or the specified
column down by 1, per problem spec). Instead of rotating in place for every
query (which would cost O(N) per query), accumulate the net shift per row
and per column first (mod N), then apply each accumulated shift once:
  1. Apply all row shifts to build an intermediate matrix.
  2. Apply all column shifts to the intermediate matrix to get the final result.

Time Complexity: O(N^2 + R + C)
  - O(R + C) to accumulate shifts
  - O(N^2) to apply row shifts and O(N^2) to apply column shifts
Space Complexity: O(N^2) for the intermediate and final matrices
"""


# ---------------------------- Solution ----------------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    ptr = 0
    N = int(data[ptr])
    R = int(data[ptr + 1])
    C = int(data[ptr + 2])
    ptr += 3
    matrix = []
    for _ in range(N):
        matrix.append([int(x) for x in data[ptr:ptr + N]])
        ptr += N
    row_shifts = [0] * N
    for _ in range(R):
        r_idx = int(data[ptr]) - 1
        row_shifts[r_idx] = (row_shifts[r_idx] + 1) % N
        ptr += 1
    col_shifts = [0] * N
    for _ in range(C):
        c_idx = int(data[ptr]) - 1
        col_shifts[c_idx] = (col_shifts[c_idx] + 1) % N
        ptr += 1
    after_row_rotations = [[0] * N for _ in range(N)]
    for i in range(N):
        shift = row_shifts[i]
        for j in range(N):
            after_row_rotations[i][(j + shift) % N] = matrix[i][j]
    final_matrix = [[0] * N for _ in range(N)]
    for j in range(N):
        shift = col_shifts[j]
        for i in range(N):
            final_matrix[(i + shift) % N][j] = after_row_rotations[i][j]
    for row in final_matrix:
        print(*(row))

if __name__ == "__main__":
    solve()
