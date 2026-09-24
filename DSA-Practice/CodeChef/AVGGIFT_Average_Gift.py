"""
Platform    : CodeChef
Problem     : Average Gift (AVGGIFT)
Link        : https://www.codechef.com/problems/AVGGIFT
Difficulty  : 1701
Topics      : Math, Observation, Ad-hoc
Date Solved : 2026-09-24

Approach:
    An average of values taken from S can never fall below min(S) or
    exceed max(S), and every value inside that range is reachable.
    So the answer is YES iff min(S) <= X <= max(S), otherwise NO.

Complexity:
    Time  : O(N) per test case (one pass each for min and max)
    Space : O(N) to store the array
"""


# ---------------------------------------- Solution ---------------------------------------------


import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, X = map(int, input().split())
    S = list(map(int, input().split()))

    if min(S) <= X <= max(S):
        print("YES")
    else:
        print("NO")
