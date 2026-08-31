"""
Problem   : Constellation
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/32/D
Difficulty: *1600
Topic     : Implementation

Approach:
For each possible radius r (1 to min(n, m)//2), scan every valid center
cell and check if it plus its four arms (up, down, left, right, each r
cells away) are all '*'. Return the k-th such constellation found, in
increasing order of radius, then row-major order of center within a
radius. If fewer than k exist, print -1.

Time complexity : O(min(n,m) * n * m) worst case (nested radius/row/col scan)
Space complexity: O(n*m) for storing the grid as bytes
"""


# -------------------------------- Solution --------------------------------


import sys

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    grid = [input().strip().encode() for _ in range(n)]
    max_r = min(n, m) // 2
    for r in range(1, max_r + 1):
        for i in range(r, n - r):
            row = grid[i]
            up = grid[i - r]
            down = grid[i + r]
            for j in range(r, m - r):
                if row[j] != 42:       
                    continue
                if (up[j] == 42 and
                        down[j] == 42 and
                        row[j - r] == 42 and
                        row[j + r] == 42):
                    k -= 1
                    if k == 0:
                        sys.stdout.write(
                            f"{i + 1} {j + 1}\n"
                            f"{i - r + 1} {j + 1}\n"
                            f"{i + r + 1} {j + 1}\n"
                            f"{i + 1} {j - r + 1}\n"
                            f"{i + 1} {j + r + 1}\n"
                        )
                        return
    print(-1)

if __name__ == "__main__":
    solve()
