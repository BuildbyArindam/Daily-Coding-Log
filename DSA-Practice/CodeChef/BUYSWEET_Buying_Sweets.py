"""
Problem   : Buying Sweets (BUYSWEET)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/BUYSWEET
Difficulty: 1706
Date      : 2026-09-24
Topics    : Greedy, Sorting, Binary Search, Math

Approach:
    Buying sweet i needs at least A[i] rupees and permanently costs A[i] - B[i].
    Reduce each sweet to (threshold = A[i], net_cost = A[i] - B[i]).
    1. Sort by threshold and keep only the Pareto frontier: sweets whose net
       cost is strictly lower than every sweet with a smaller threshold.
       Thresholds increase and net costs decrease along the frontier.
    2. Greedy: with R rupees, the best choice is the affordable sweet with the
       lowest net cost, i.e. the last frontier entry with threshold <= R
       (found by binary search).
    3. Buy it k = (R - threshold) // cost + 1 times in one step, until R drops
       below its threshold. Then repeat with the remaining R.
    Each round moves to a strictly smaller frontier index, so the loop runs at
    most |frontier| times.

Complexity:
    Time : O(N log N) per test case (sort + up to N binary searches)
    Space: O(N)
"""


# --------------------------------------- Solution -------------------------------------------


import sys
from bisect import bisect_right

def solve():
    input = sys.stdin.readline
    T = int(input())
    ans = []
    for _ in range(T):
        N, R = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        sweets = [(A[i], A[i] - B[i]) for i in range(N)]
        sweets.sort()
        thresholds = []
        costs = []
        best = 10**30
        for a, c in sweets:
            if c < best:
                best = c
                thresholds.append(a)
                costs.append(c)
        count = 0
        while thresholds:
            idx = bisect_right(thresholds, R) - 1
            if idx < 0:
                break
            threshold = thresholds[idx]
            cost = costs[idx]
            k = (R - threshold) // cost + 1
            count += k
            R -= k * cost
        ans.append(str(count))
    print("\n".join(ans))

if __name__ == "__main__":
    solve()
