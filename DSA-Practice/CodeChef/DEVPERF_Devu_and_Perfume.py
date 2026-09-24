"""
Problem   : Devu and Perfume (DEVPERF)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/DEVPERF
Difficulty: 1708
Date      : 2026-09-24
Topics    : Implementation, Grid, Observation / Math

Approach:
    Scan the grid once and track the bounding box of all '*' cells
    (min/max row and column). The larger of the row span and the column
    span is the "diameter" of the point set. Spreading from the center
    covers that diameter in ceil(diameter / 2) steps, and the extra
    +1 accounts for the initial step. If the grid has no '*', the answer is 0.

Complexity:
    Time  : O(T * N * M), one pass over every cell
    Space : O(1) extra (only the row being read is held in memory)
"""


# --------------------------------------------- Solution ------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        min_r = n
        max_r = -1
        min_c = m
        max_c = -1
        for r in range(n):
            row = input().strip()
            for c, ch in enumerate(row):
                if ch == '*':
                    min_r = min(min_r, r)
                    max_r = max(max_r, r)
                    min_c = min(min_c, c)
                    max_c = max(max_c, c)
        if max_r == -1:
            print(0)
            continue
        row_span = max_r - min_r
        col_span = max_c - min_c
        diameter = max(row_span, col_span)
        spread_time = (diameter + 1) // 2
        print(1 + spread_time)

if __name__ == "__main__":
    solve()
