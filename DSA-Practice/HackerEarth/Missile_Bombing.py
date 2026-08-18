"""
Problem   : Missile Bombing
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/missile-bombing-cd56ab51/
Difficulty: Easy
Topic     : Basic Programming, Basics of Implementation, Implementation
Date      : 2026-08-18

Approach:
    Each missile P bombs a rectangular sub-grid (A..C rows, B..D cols),
    toggling (XOR) every cell it hits. Instead of updating each cell in
    the rectangle directly (too slow for large grids), use a 2D XOR
    difference array: mark the four corners of the rectangle with P,
    then recover final cell values via a 2D prefix-XOR pass (XOR is its
    own inverse, so this works exactly like a prefix-sum difference
    array, just with ^= instead of +=).

    Steps:
      1. For each missile, XOR P at diff[A][B], diff[A][D+1],
         diff[C+1][B], diff[C+1][D+1].
      2. Row-wise prefix XOR (left to right).
      3. Column-wise prefix XOR (top to bottom).
      4. Result at diff[i][j] = number of missiles hitting (i, j) mod 2,
         i.e., whether cell (i, j) has been bombed an odd number of times.

Time Complexity : O(M + N^2)   -- M updates (O(1) each) + O(N^2) grid pass
Space Complexity: O(N^2)       -- the difference/grid array
"""


# -------------------------- Solution ----------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    N = int(data[0])
    M = int(data[1])
    diff = [[0] * (N + 2) for _ in range(N + 2)]
    idx = 2
    for _ in range(M):
        P = int(data[idx])
        A = int(data[idx + 1])
        B = int(data[idx + 2])
        C = int(data[idx + 3])
        D = int(data[idx + 4])
        idx += 5
        diff[A][B] ^= P
        diff[A][D + 1] ^= P
        diff[C + 1][B] ^= P
        diff[C + 1][D + 1] ^= P
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            diff[i][j] ^= diff[i][j - 1]
    out = []
    for i in range(1, N + 1):
        row = []
        for j in range(1, N + 1):
            diff[i][j] ^= diff[i - 1][j]
            row.append(str(diff[i][j]))
        out.append(" ".join(row))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()
