"""
Problem   : Journey
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/43/D
Difficulty: *2000
Topics    : brute force, constructive algorithms, implementation
Date      : 2026-09-11

Approach:
    The kingdom is an n x m grid; the tour must start and end at the
    capital (1,1), visit every cell exactly once, and move only to
    edge-adjacent cells -- except for teleports, which can jump anywhere
    but are limited/costed, so we minimize their count.

    - If n == 1 or m == 1 (a single row/column):
        - length == 2 -> a direct Hamiltonian cycle exists (0 teleports).
        - length > 2  -> walk straight to the far end, then teleport
                         back to (1,1) (1 teleport).
    - If n or m is even (and both > 1):
        Build an explicit Hamiltonian cycle: traverse the first row
        left->right, snake through the remaining rows over columns
        2..m, then return up column 1 to (1,1). If only m is even,
        solve for the transposed grid and swap coordinates back.
        -> 0 teleports needed.
    - If both n and m are odd (and > 1):
        No Hamiltonian cycle exists on an odd x odd grid, so snake
        through the whole grid as a Hamiltonian PATH, then use exactly
        one teleport from the path's last cell back to (1,1).
        -> 1 teleport needed.

Complexity:
    Time : O(n*m)  -- every cell is visited/emitted once.
    Space: O(n*m)  -- path list stores every grid cell.
"""


# ---------------------- Solution ----------------------------------


import sys

def cycle_for_even_n(n, m):
    """
    Hamiltonian cycle for n even, n >= 2, m >= 2.

    Route:
      first row left -> right
      rows 2..n snake through columns 2..m
      column 1 bottom -> top
      back to (1,1)
    """
    path = []
    for c in range(1, m + 1):
        path.append((1, c))
    for r in range(2, n + 1):
        if r % 2 == 0:
            for c in range(m, 1, -1):
                path.append((r, c))
        else:
            for c in range(2, m + 1):
                path.append((r, c))
    for r in range(n, 1, -1):
        path.append((r, 1))
    path.append((1, 1))
    return path

def solve():
    n, m = map(int, sys.stdin.readline().split())
    if n == 1 or m == 1:
        length = max(n, m)
        if length == 2:
            print(0)
            print(1, 1)
            print(1 if n == 1 else 2, 2 if n == 1 else 1)
            print(1, 1)
            return
        path = []
        if n == 1:
            for c in range(1, m + 1):
                path.append((1, c))
            end = (1, m)
        else:
            for r in range(1, n + 1):
                path.append((r, 1))
            end = (n, 1)
        print(1)
        print(end[0], end[1], 1, 1)
        for x, y in path:
            print(x, y)
        print(1, 1)
        return
    if n % 2 == 0:
        path = cycle_for_even_n(n, m)
        print(0)
        for x, y in path:
            print(x, y)
    elif m % 2 == 0:
        path_t = cycle_for_even_n(m, n)
        path = [(y, x) for x, y in path_t]
        print(0)
        for x, y in path:
            print(x, y)
    else:
        path = []
        for r in range(1, n + 1):
            if r % 2 == 1:
                for c in range(1, m + 1):
                    path.append((r, c))
            else:
                for c in range(m, 0, -1):
                    path.append((r, c))
        end_x, end_y = path[-1]
        print(1)
        print(end_x, end_y, 1, 1)
        for x, y in path:
            print(x, y)
        print(1, 1)

if __name__ == "__main__":
    solve()
