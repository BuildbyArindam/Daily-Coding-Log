"""
Problem   : The One with All the Candy
Platform  : CodeChef (S07E09)
Link      : https://www.codechef.com/problems/S07E09
Difficulty: 1804
Date      : 2026-10-10
Topics    : 1D Arrays, Sorting, Observation, Data Structures

Approach:
    The answer depends only on the minimum value and how many times it
    occurs. Every element needs at least `min` units, so the base cost is
    min * N. Each element strictly above the minimum (N - count_of_min of
    them) adds exactly one extra unit. No sorting is needed: one pass for
    the min and one for its count.

Complexity:
    Time : O(N) per test case
    Space: O(N) for the input array (O(1) extra)
"""


# ----------------------------------------------- Solution -------------------------------------------------


import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    minimum = min(A)
    count = A.count(minimum)
    ans = minimum * N + (N - count)
    print(ans)
