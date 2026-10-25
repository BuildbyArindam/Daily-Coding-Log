"""
Problem   : K Distinct Array (DISTK)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/DISTK
Difficulty: 2015
Topics    : Constructive, Greedy, Math
Date      : 2026-10-25

Approach:
    Greedily pick the largest p such that the array 1..p followed by
    (n - p) repeated elements still has a minimum count <= k. The leftover
    amount (k - minimum) is absorbed by choosing the repeated value
    v = p - extra, so the final count is exactly k.

Complexity:
    Time : O(n) per test case (p <= n, plus O(n) output construction)
    Space: O(n) for the output array
"""


# --------------------------------------------- Solution -------------------------------------------------------------


import sys

def build(n, k):
    p = 1
    while p < n and (p + 1) * (p + 2) // 2 + (n - p - 1) <= k:
        p += 1
    out = list(range(1, p + 1))
    if p == n:
        return out
    extra = k - (p * (p + 1) // 2 + (n - p))
    v = p - extra
    out += [v] * (n - p)
    return out

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    res = []
    for i in range(t):
        n = int(data[1 + 2 * i])
        k = int(data[2 + 2 * i])
        res.append(' '.join(map(str, build(n, k))))
    sys.stdout.write('\n'.join(res) + '\n')

main()
