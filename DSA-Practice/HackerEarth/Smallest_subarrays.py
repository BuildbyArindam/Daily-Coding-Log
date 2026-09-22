"""
Problem: Smallest Subarrays
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/smallest-subarray-2-d6530e0b/
Date Solved: 2026-09-22
Difficulty: Medium
Topics: Binary Search, Fenwick Tree (BIT), Order Statistics

Approach:
For each index i, we need the smallest subarray starting at i that contains
at least B[i] elements greater than or equal to A[i]. Process indices in
decreasing order of A[i] (grouping ties together) and activate them in a
Fenwick Tree indexed by position. When querying for index i, all elements
with A[] >= A[i] are already active, so `before` = count of such elements
to the left of i, and we binary-search (via BIT k-th order statistic) for
the position of the (before + B[i])-th active element from the left,
which gives the right boundary of the minimal subarray.

Time Complexity: O(N log N)   -- sorting + Fenwick updates/queries, each O(log N)
Space Complexity: O(N)        -- Fenwick tree array + auxiliary arrays
"""


# ------------------------------------------ Solution ---------------------------------------------


import sys

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
    def update(self, idx, value):
        while idx <= self.n:
            self.bit[idx] += value
            idx += idx & -idx
    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.bit[idx]
            idx -= idx & -idx
        return res
    def kth(self, k):
        idx = 0
        step = 1 << (self.n.bit_length() - 1)
        while step:
            nxt = idx + step
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            step >>= 1
        return idx + 1

def solve():
    input = sys.stdin.buffer.readline
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    order = sorted(range(N), key=lambda i: A[i], reverse=True)
    bit = FenwickTree(N)
    ans = [-1] * N
    p = 0
    while p < N:
        q = p
        while q < N and A[order[q]] == A[order[p]]:
            q += 1
        for x in range(p, q):
            idx = order[x] + 1  
            bit.update(idx, 1)
        for x in range(p, q):
            i = order[x] + 1     
            need = B[i - 1]
            before = bit.query(i - 1)
            target = before + need
            total_active = bit.query(N)
            if target <= total_active:
                pos = bit.kth(target)
                ans[i - 1] = pos - i + 1
        p = q
    print(*ans)

if __name__ == "__main__":
    solve()
