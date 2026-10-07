"""
Problem   : Code Apocalypse 3.0 ..Coming SOON ![Easy-Medium]
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/code-apocalypse-30-coming-soon/
Date      : 2026-10-07
Difficulty: Medium
Topics    : Binary Search, Math

Approach  : The feasibility check is monotonic in k, so binary search applies.
            Rearranging k*X - (N-k)*Y <= M gives k*(X+Y) <= M + N*Y,
            which solves directly as k = (M + N*Y) // (X+Y), capped at N.
            This replaces the O(log N) search with an O(1) formula.

Complexity: Time  O(T)  (O(1) per test case)
            Space O(1)
"""


# ------------------------------------------------ Solution ---------------------------------------------


import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M, X, Y = map(int, input().split())
    ans = min(N, (M + N * Y) // (X + Y))
    print(ans)
