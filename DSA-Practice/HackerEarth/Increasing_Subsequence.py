"""
Problem   : Increasing Subsequence
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/increasing-subsequence-1-2d4df2d3/
Difficulty: Medium
Topics    : Fenwick Tree (BIT), Advanced Data Structures
Date      : 2026-09-28

Approach:
    Find a strictly increasing subsequence of length k that maximizes
    (last - first), or print -1 if none exists.
    - Special cases: k == 1 -> 0; k == 2 -> single pass tracking the running
      minimum (O(n)).
    - General case: coordinate-compress the values, then keep one Fenwick tree
      per length L (1..k). Tree L stores, for each value rank, the minimum
      possible starting element of an increasing subsequence of length L
      ending at that value (prefix-min queries).
    - For each element x with rank r: set tree[1] at r to x, then for
      L = 2..k, query tree[L-1] over ranks < r and, if a start exists,
      update tree[L] at r. At L == k, candidate energy = x - start.

Complexity:
    Time  : O(n * k * log n)  (O(n) for k <= 2)
    Space : O(k * m), where m = number of distinct values
"""


# ------------------------------------- Solution --------------------------------------------


import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, k = data[0], data[1]
    a = data[2:2 + n]
    if k == 1:
        print(0)
        return
    if k == 2:
        min_seen = 10**18
        ans = -1
        for x in a:
            if min_seen < x:
                ans = max(ans, x - min_seen)
            if x < min_seen:
                min_seen = x
        print(ans)
        return
    values = sorted(set(a))
    rank = {v: i + 1 for i, v in enumerate(values)}
    m = len(values)
    INF = 10**18
    bit = [[INF] * (m + 1) for _ in range(k + 1)]
    def query(tree, idx):
        res = INF
        while idx > 0:
            v = tree[idx]
            if v < res:
                res = v
            idx -= idx & -idx
        return res
    def update(tree, idx, value):
        while idx <= m:
            if value < tree[idx]:
                tree[idx] = value
            idx += idx & -idx
    answer = -1
    for x in a:
        r = rank[x]
        update(bit[1], r, x)
        for length in range(2, k + 1):
            start = query(bit[length - 1], r - 1)
            if start != INF:
                update(bit[length], r, start)
                if length == k:
                    energy = x - start
                    if energy > answer:
                        answer = energy
    print(answer)

if __name__ == "__main__":
    solve()
