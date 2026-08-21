"""
Problem   : Flag
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/16/A
Difficulty: *800
Topic     : Implementation
Date      : 2026-08-21

Approach:
Read the grid of n rows x m columns. A valid flag requires each row to be
a single repeated character (uniform row) and no two adjacent rows can
share the same character (else the stripe boundary disappears). Check both
conditions in one pass: verify row uniformity via set(row) == 1 element,
and compare grid[i][0] with grid[i-1][0] for the adjacency check.

Time Complexity : O(n * m)  -> each row scanned once to build the set
Space Complexity: O(n * m)  -> input stored as list of strings
"""


# ------------------------- Solution ------------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    grid = data[2:]
    for i in range(n):
        if len(set(grid[i])) != 1:
            print("NO")
            return
        if i > 0 and grid[i][0] == grid[i - 1][0]:
            print("NO")
            return
    print("YES")

if __name__ == "__main__":
    solve()
