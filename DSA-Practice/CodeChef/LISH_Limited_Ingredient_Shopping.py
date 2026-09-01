"""
Problem   : Limited Ingredient Shopping
Platform  : CodeChef
Link      : https://www.codechef.com/problems/LISH
Date      : 2026-09-01
Difficulty: Cakewalk
Topics    : Greedy, Sorting, Basic Math

Approach:
Each item can be bought at most twice (contributes weight x, x again).
To minimize the number of items needed to reach total weight >= W,
greedily pick the heaviest available weights first. Duplicate every
element (since each item is available twice), sort all 2N weights in
descending order, then accumulate from the top until the running sum
reaches W. The index at which this happens is the minimum count.
If the full sum of all 2N weights is still < W, it's impossible (-1).

Time Complexity : O(N log N)  -- dominated by sorting 2N elements
Space Complexity: O(N)        -- storage for the duplicated weights list
"""


# ------------------------ Solution ------------------------------


W = int(input())
N = int(input())
A = list(map(int, input().split()))
weights = []
for x in A:
    weights.append(x)
    weights.append(x)
weights.sort(reverse=True)
total = 0
for i, x in enumerate(weights, start=1):
    total += x
    if total >= W:
        print(i)
        break
else:
    print(-1)
