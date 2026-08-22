"""
Problem   : Hawkeye and Floodfill (Easy)
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/hawkeye-and-floodfill/
Date      : 2026-08-22
Topic     : Basic Programming / Implementation (Grid, Chebyshev Distance)

Approach:
    For each cell (r, c) on an n x n grid, compute the Chebyshev distance
    (chessboard distance) from the source cell (i, j) as:
        dist = max(|r - i|, |c - j|)
    The "impact" at that cell decays linearly with distance from power p:
        impact = max(0, p - dist)
    This naturally floods outward in a square ring pattern (like a king's
    move radius in chess) rather than a diamond (Manhattan) pattern.

Time Complexity  : O(n^2)  -- every cell visited once
Space Complexity : O(n^2)  -- output buffer for the grid (O(1) extra if
                              printing row-by-row instead of buffering)
"""


# -------------------------- Solution -----------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    i = int(input_data[1])
    j = int(input_data[2])
    p = int(input_data[3])
    output = []
    for r in range(n):
        row = []
        for c in range(n):
            dist = max(abs(r - i), abs(c - j))
            impact = max(0, p - dist)
            row.append(str(impact))
        output.append(" ".join(row))
    print("\n".join(output))

if __name__ == "__main__":
    solve()
