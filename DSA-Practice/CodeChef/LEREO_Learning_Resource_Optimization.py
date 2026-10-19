"""
Platform   : CodeChef
Problem    : Learning Resource Optimization (LEREO)
Link       : https://www.codechef.com/problems/LEREO
Difficulty : 2316
Date       : 2026-10-19
Topics     : Dynamic Programming, Grouped Knapsack

Approach:
    Grouped 0/1 knapsack over the budget `cap`. For each group, two
    options are computed from the same previous state `before`:
      1. Buy items individually: standard 0/1 knapsack over the group's
         items, starting from a copy of `before`.
      2. Buy the group's bundle: pay bundle_cost[g] once and gain the
         sum of all member values, transitioning from `before`.
    The better of the two is kept per budget, and the result becomes the
    state for the next group. Answer = max(best).

Complexity (N items, M groups, budget C):
    Time  : O(N*C + M*C)
    Space : O(N + M + C)  (dp arrays are copied once per group)
"""


# ---------------------------------------------- Solution ------------------------------------------------------------------


import sys

def main():
    tokens = sys.stdin.read().split()
    pos = 0
    n, m, cap = int(tokens[0]), int(tokens[1]), int(tokens[2])
    pos = 3
    members = [[] for _ in range(m + 1)]
    for _ in range(n):
        g = int(tokens[pos])
        c = int(tokens[pos + 1])
        val = int(tokens[pos + 2])
        pos += 3
        members[g].append((c, val))
    bundle_cost = [0] * (m + 1)
    for j in range(1, m + 1):
        bundle_cost[j] = int(tokens[pos])
        pos += 1
    best = [0] * (cap + 1)
    for grp in range(m, 0, -1):
        items = members[grp]
        if not items:
            continue
        before = best[:]
        after = before[:]
        for c, val in items:
            for w in range(cap, c - 1, -1):
                cand = after[w - c] + val
                if cand > after[w]:
                    after[w] = cand
        bc = bundle_cost[grp]
        total_val = sum(v for _, v in items)
        for w in range(bc, cap + 1):
            cand = before[w - bc] + total_val
            if cand > after[w]:
                after[w] = cand
        best = after
    print(max(best))

main()
