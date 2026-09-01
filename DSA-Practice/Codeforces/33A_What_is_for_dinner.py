"""
Problem   : What is for dinner?
Link      : https://codeforces.com/problemset/problem/33/A
Date      : 2026-09-01
Difficulty: *1200 (Codeforces)
Topics    : Greedy, Implementation

Approach:
Cats are served food in fixed rows, and only the minimum food
quantity in each row is "safe" for every cat to eat (viability
per row). Track the minimum c per row r using an array indexed
by row, sum these minimums across all rows to get the max total
food eatable, then cap it at k (the number of biscuits available).

Time complexity : O(n + m)   -- one pass over n biscuits, one sum over m rows
Space complexity: O(m)       -- min_viability array indexed by row
"""


# ------------------------- Solution --------------------------------


import sys

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    # Minimum viability in each row
    min_viability = [10**18] * (m + 1)
    for _ in range(n):
        r, c = map(int, input().split())
        min_viability[r] = min(min_viability[r], c)
    max_eatable = sum(min_viability[1:])
    print(min(k, max_eatable))

if __name__ == "__main__":
    solve()
