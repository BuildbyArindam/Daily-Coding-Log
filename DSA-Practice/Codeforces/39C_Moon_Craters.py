"""
Problem: Moon Craters
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/39/C
Difficulty: *2100
Topics: DP, Sortings
Date solved: 2026-09-06

Approach:
Each crater is an interval [c-r, c+r]. A crater j can be "erased" by
crater i only if j is strictly nested inside i (with tangency at
endpoints allowed). This forms a nesting forest over the intervals.
Sort intervals by right endpoint (ties broken by left endpoint
descending) so containment checks become prefix-compatible, and
precompute prev[i] = last interval disjoint from i (via binary
search on right endpoints). Two layers of weighted interval
scheduling DP are then applied:
  1. w[i]: max craters in the "family" rooted at crater i, found by
     running a knapsack-style DP over intervals nested inside i,
     picking a disjoint subset of direct children to maximize
     sum(w[child]).
  2. A top-level DP over all intervals (again weighted interval
     scheduling, using prev[]) selects the disjoint set of outermost
     ("root") craters maximizing total w[i].
The nesting structure is then reconstructed top-down (recomputing
each parent's child-selection DP, O(n) per level) to output the
countable craters and their assigned parent-child relationships.

Time complexity: O(n^2)   (n^2 DP for w[i], reconstruction is O(n) per
                            node so O(n^2) worst case overall)
Space complexity: O(n^2)  (temp_dp/choice reused per call, O(n) each;
                            overall auxiliary arrays are O(n))
"""


# -------------------------- Solution ---------------------------------


import sys
from bisect import bisect_right

def solve():
    input = sys.stdin.readline
    n = int(input())
    intervals = []
    for idx in range(n):
        c, r = map(int, input().split())
        l = c - r
        rr = c + r
        intervals.append((rr, -l, l, idx))
    intervals.sort()
    L = [x[2] for x in intervals]
    R = [x[0] for x in intervals]
    original_id = [x[3] for x in intervals]
    prev = [0] * n
    for i in range(n):
        prev[i] = bisect_right(R, L[i], 0, i) - 1
    w = [0] * n
    dp = [0] * (n + 1)
    for i in range(n):
        dp[0] = 0
        li, ri = L[i], R[i]
        for j in range(i):
            best = dp[j]
            if L[j] >= li and R[j] <= ri:
                take = dp[prev[j] + 1] + w[j]
                if take > best:
                    best = take
            dp[j + 1] = best
        w[i] = dp[i] + 1
    dp = [0] * (n + 1)
    take_global = [False] * n
    for i in range(n):
        skip = dp[i]
        take = dp[prev[i] + 1] + w[i]
        if take > skip:
            dp[i + 1] = take
            take_global[i] = True
        else:
            dp[i + 1] = skip
    roots = []
    p = n
    while p > 0:
        i = p - 1
        if take_global[i]:
            roots.append(i)
            p = prev[i] + 1
        else:
            p -= 1
    temp_dp = [0] * (n + 1)
    choice = [False] * n
    def get_children(i):
        li, ri = L[i], R[i]
        temp_dp[0] = 0
        for j in range(i):
            best = temp_dp[j]
            choice[j] = False
            if L[j] >= li and R[j] <= ri:
                cand = temp_dp[prev[j] + 1] + w[j]
                if cand > best:
                    best = cand
                    choice[j] = True
            temp_dp[j + 1] = best
        children = []
        p = i
        while p > 0:
            j = p - 1
            if choice[j]:
                children.append(j)
                p = prev[j] + 1
            else:
                p -= 1
        return children
    answer = []
    stack = roots[:]
    while stack:
        i = stack.pop()
        answer.append(original_id[i] + 1)
        children = get_children(i)
        stack.extend(children)
    print(len(answer))
    print(*answer)

if __name__ == "__main__":
    solve()
