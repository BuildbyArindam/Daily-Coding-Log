"""
Problem   : Blinds (Codeforces 38C)
Link      : https://codeforces.com/problemset/problem/38/C
Date      : 2026-09-04
Difficulty: *1400
Topic     : Brute Force

Approach:
For every possible cut length d (from l up to max(a)), compute how many
full pieces of length d each strip a[i] yields (a[i] // d), sum them up
across all strips, and track the best d * total_pieces product. The
optimal window width is always d * (a[i] // d) for some strip and some
d in [l, max(a)], so brute-forcing d covers all candidates.

Time complexity : O(n * (max(a) - l))  -- for each d, scan all n strips
Space complexity: O(n)                 -- just the input array
"""


# ----------------------- Solution -----------------------------------


n, l = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for d in range(l, max(a) + 1):
    pieces = 0
    for x in a:
        pieces += x // d
    ans = max(ans, pieces * d)
print(ans)
