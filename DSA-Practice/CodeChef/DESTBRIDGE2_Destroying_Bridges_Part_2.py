"""
Problem : Destroying Bridges Part 2 (CodeChef, DESTBRIDGE2)
Link    : https://www.codechef.com/problems/DESTBRIDGE2
Date    : 2026-10-16
Difficulty: 2005
Topics  : Sorting, Prefix Sums, Greedy, Math

Approach:
  - vals[0] is the fixed element; sort the remaining values and build prefix sums.
  - For each group size k, the group is vals[0] plus (k-1) others, with sum s
    and cost s * (G - s), where G is the total sum.
  - The cost is concave in s, so its minimum over all valid groups is at an
    extreme of s. It is enough to check the (k-1) smallest and the (k-1)
    largest others, both read off the prefix sums in O(1).
  - Return the smallest k whose best cost is <= cap. At k = n the cost is 0,
    so an answer always exists.

Complexity (per test case):
  Time  : O(n log n) for the sort, plus O(n) for the scan over k
  Space : O(n) for the sorted list and prefix sums
"""


# -------------------------------------------- Solution -------------------------------------------------------


import sys

def solve_case(cap, vals):
    n = len(vals)
    first = vals[0]
    rest = sorted(vals[1:])
    grand = first + sum(rest)
    pre = [0]
    for v in rest:
        pre.append(pre[-1] + v)
    k = 1
    while k <= n:
        take = k - 1
        low_s = first + pre[take]                 
        high_s = first + pre[-1] - pre[len(rest) - take]  
        best = min(low_s * (grand - low_s), high_s * (grand - high_s))
        if best <= cap:
            return k
        k += 1
    return n

def main():
    tokens = sys.stdin.read().split()
    ptr = 0
    t = int(tokens[ptr]); ptr += 1
    out = []
    for _ in range(t):
        n = int(tokens[ptr]); c = int(tokens[ptr + 1]); ptr += 2
        arr = [int(x) for x in tokens[ptr:ptr + n]]
        ptr += n
        out.append(str(solve_case(c, arr)))
    print("\n".join(out))

main()
