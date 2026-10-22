"""
Platform   : CodeChef
Problem    : Minimum Incompatibility Partition (MINP)
Link       : https://www.codechef.com/problems/MINP
Difficulty : 1650
Date       : 2026-10-22
Topics     : Bitmask DP, Sorting, Combinatorics

Approach:
  1. Sort the array, then precompute every valid group: a subset of size
     n/k with all-distinct values. Its cost is max - min, which is
     last - first because the array is sorted. Groups are stored in a
     dict keyed by their bitmask.
  2. dp[mask] = minimum total cost to partition the elements in `mask`
     into complete groups.
  3. From each reachable mask, always put the lowest unused index into
     the next group and choose the other (n/k - 1) members from the
     remaining free indices. Fixing the lowest bit makes each partition
     get built in only one order, which removes permutation blowup.
  4. The answer is dp[full_mask], or -1 if it is unreachable.

Complexity (n = array size, w = n/k group size):
  Time  : O(C(n, w) * w) for precomputation
          + O(2^n * C(n, w-1)) worst-case for the DP transitions
  Space : O(2^n + C(n, w))
"""


# -------------------------------------------- Solution -----------------------------------------------------------------


import sys
from itertools import combinations

def main():
    tokens = sys.stdin.read().split()
    total, parts = int(tokens[0]), int(tokens[1])
    seq = sorted(int(t) for t in tokens[2:2 + total])
    width = total // parts
    group_cost = {}
    for pick in combinations(range(total), width):
        chosen = [seq[i] for i in pick]
        if len(set(chosen)) != width:
            continue
        code = 0
        for i in pick:
            code |= 1 << i
        group_cost[code] = chosen[-1] - chosen[0]
    everything = (1 << total) - 1
    BIG = float("inf")
    best = [BIG] * (everything + 1)
    best[0] = 0
    for state in range(everything):
        cur = best[state]
        if cur == BIG:
            continue
        lowbit = (~state) & (state + 1)
        pos = lowbit.bit_length() - 1
        free = [j for j in range(pos + 1, total) if not (state >> j) & 1]
        if len(free) < width - 1:
            continue
        for extra in combinations(free, width - 1):
            code = lowbit
            for j in extra:
                code |= 1 << j
            price = group_cost.get(code)
            if price is None:
                continue
            nxt = state | code
            cand = cur + price
            if cand < best[nxt]:
                best[nxt] = cand
    answer = best[everything]
    print(-1 if answer == BIG else answer)

main()
