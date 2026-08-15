"""
Problem   : Maximize!
Link      : https://codeforces.com/contest/939/problem/E
Platform  : Codeforces
Difficulty: 1800
Topics    : Binary Search, Greedy, Ternary Search, Two Pointers
Date      : 2026-08-15

Approach:
  - Values are added in strictly increasing order (guaranteed by the
    problem), so the array is always implicitly sorted as it grows —
    the newest element a[n] is always the current maximum.
  - For a fixed a[n], we want to choose a prefix [1..cur] whose average
    minimizes total, maximizing a[n] - avg(prefix). The average of a
    prefix as a function of its length is unimodal (convex-ish), so an
    amortized two-pointer (`cur` only moves forward) finds the optimal
    prefix length in total O(n) across all insertions instead of
    re-searching from scratch each time.
  - ans is updated only on insert; type-2 queries just report current ans.

Time Complexity : O(Q) amortized (two-pointer moves forward only, total
                   work across all insertions is O(n))
Space Complexity: O(Q) for storing the array
"""


# ---------------------- Solution --------------------------


import sys
input = sys.stdin.readline
Q = int(input())
a = [0] * (Q + 1)
n = 0
cur = 0
total = 0
ans = 0.0

for _ in range(Q):
    query = list(map(int, input().split()))
    op = query[0]
    if op == 1:
        x = query[1]
        n += 1
        a[n] = x
        if n == 1:
            continue
        if cur == 0:
            cur = 1
            total = a[1]
        while (
            cur < n - 1
            and (total + a[n]) * (cur + 2)
            > (cur + 1) * (total + a[n] + a[cur + 1])
        ):
            cur += 1
            total += a[cur]
        ans = max(
            ans,
            a[n] - (total + a[n]) / (cur + 1)
        )
    else:
        print(f"{ans:.9f}")
      
