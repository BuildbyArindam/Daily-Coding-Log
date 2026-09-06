"""
Problem   : Company Income Growth
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/39/B
Date      : 2026-09-06
Difficulty: *1300
Topic     : Greedy

Approach:
Scan the income sequence once, tracking the next "expected" value
(starting at 1) needed to continue a strictly increasing run from 1.
Whenever the current income equals `expected`, record that year and
bump `expected` by 1. This greedily picks the earliest possible years
to claim credit for growth, since skipping a match can only delay
reaching later expected values.

Time complexity : O(n)  — single pass over the array
Space complexity: O(n)  — worst case, all years qualify
"""


# --------------------------- Solution -----------------------------------


n = int(input())
a = list(map(int, input().split()))
expected = 1
years = []
for i in range(n):
    if a[i] == expected:
        years.append(2000 + i + 1) 
        expected += 1
if not years:
    print(0)
else:
    print(len(years))
    print(*years)
