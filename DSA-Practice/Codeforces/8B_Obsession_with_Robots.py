"""
Problem: Obsession with Robots
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/8/B
Date Solved: 2026-08-17
Difficulty: *1400
Topics: Constructive Algorithms, Graphs, Implementation

Approach:
Simulate the robot's path on a grid, tracking visited cells in a set.
At each step, before committing the move, check two failure conditions:
  1. The new cell (nx, ny) was already visited -> path crosses itself -> BUG.
  2. The new cell has more than one already-visited neighbor (excluding the
     cell we just came from) -> the path is adjacent to a non-consecutive
     part of itself -> BUG.
If the path completes without triggering either condition, print OK.

Time Complexity: O(n) - single pass over the path string, O(1) work per step
                  (checking 4 fixed neighbor offsets, O(1) set lookups).
Space Complexity: O(n) - visited set stores at most n+1 grid cells.
"""


# -------------------- Solution ---------------------------


import sys

def solve():
    s = sys.stdin.read().split()
    if not s:
        return
    path = s[0]
    moves = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}
    x, y = 0, 0
    visited = {(x, y)}
    for step in path:
        dx, dy = moves[step]
        nx, ny = x + dx, y + dy
        if (nx, ny) in visited:
            print("BUG")
            return
        for ddx, ddy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            adj_x, adj_y = nx + ddx, ny + ddy
            if (adj_x, adj_y) in visited and (adj_x, adj_y) != (x, y):
                print("BUG")
                return
        x, y = nx, ny
        visited.add((x, y))
    print("OK")

if __name__ == "__main__":
    solve()
