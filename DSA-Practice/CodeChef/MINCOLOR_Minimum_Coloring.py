# Problem: Minimum Coloring
# Link: https://www.codechef.com/problems/MINCOLOR
# Date Solved: 2026-09-25
# Difficulty: 1713
# Topics: Constructive Algorithms, Ad-hoc / Grid Construction, Parity / Bipartite Coloring, Graph Coloring
#
# Approach:
#   Checkerboard (parity) coloring: color cell (i, j) by (i + j) % 2.
#   - If the two given special cells (x1,y1) and (x2,y2) lie on different
#     parities, a straight 2-coloring already separates them -> answer uses
#     colors {1, 2}.
#   - If they share the same parity, the checkerboard alone would put both
#     cells in the same color class, so build the 2-coloring with {1, 3}
#     and then force-repaint the second special cell to color 2, giving a
#     3rd distinct value only where needed.
#   This guarantees adjacent cells differ in color (checkerboard property)
#   while keeping the two marked cells in different color classes, using
#   the minimum number of colors possible for the constraint.
#
# Time Complexity:  O(N*M) per test case  ->  O(sum(N*M)) overall
# Space Complexity: O(N*M) for the output grid (O(M) if streamed row-by-row)


# ---------------------------------------- Solution ------------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        x1, y1 = map(int, input().split())
        x2, y2 = map(int, input().split())
        p1 = (x1 + y1) % 2
        p2 = (x2 + y2) % 2
        ans = []
        if p1 != p2:
            for i in range(1, N + 1):
                row = []
                for j in range(1, M + 1):
                    if (i + j) % 2 == p1:
                        row.append(1)
                    else:
                        row.append(2)
                ans.append(row)
        else:
            for i in range(1, N + 1):
                row = []
                for j in range(1, M + 1):
                    if (i + j) % 2 == p1:
                        row.append(1)
                    else:
                        row.append(3)
                ans.append(row)
            ans[x2 - 1][y2 - 1] = 2
        for row in ans:
            print(*row)

if __name__ == "__main__":
    solve()
