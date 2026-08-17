"""
Problem   : Start of the Season
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/12/E
Rating    : *2100
Tags      : constructive algorithms, combinatorics
Date      : 2026-08-17

Approach:
---------
Construct an n x n symmetric "magic matrix" (n guaranteed even) where:
  - main diagonal is all zeros
  - each row contains every value 0..n-1 exactly once (Latin-square-like)
This models a round-robin schedule: grid[i][j] = day on which team i
plays team j.

Uses the classic "circle method" for round-robin scheduling:
  - Fix team (n-1) as the pivot; teams 0..n-2 sit on a circle of size (n-1).
  - For two non-pivot teams i, j: they meet on day (i + j) mod (n-1).
    This is a standard identity from circle-method scheduling — rotating
    team j by a fixed offset relative to i always lands on the same
    "day" index modulo (n-1), guaranteeing each row gets a distinct day
    for each opponent among 0..n-2.
  - For team i vs the pivot (n-1): they meet on day (2*i) mod (n-1),
    the one day left unused by team i among the non-pivot matches.
  - Day values are shifted by +1 to reserve 0 for "no match" (diagonal).

Correctness sketch: for fixed i, as j ranges over all teams != i,
(i+j) mod (n-1) takes each residue in [0, n-2] exactly once except the
residue matching i vs itself, which is exactly filled by the pivot-day
formula (2*i) mod (n-1) — so every row is a permutation of 0..n-1.

Complexity:
-----------
Time  : O(n^2)  -- fill an n x n grid once
Space : O(n^2)  -- store the grid (required for output)
"""


# ------------------- Solution -------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    grid = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        for j in range(n - 1):
            if i == j:
                grid[i][j] = 0
            else:
                val = (i + j) % (n - 1) + 1
                grid[i][j] = val
    for i in range(n - 1):
        diag_val = (2 * i) % (n - 1) + 1
        grid[i][n - 1] = diag_val
        grid[n - 1][i] = diag_val
    grid[n - 1][n - 1] = 0
    for row in grid:
        print(*(row))

if __name__ == '__main__':
    solve()
