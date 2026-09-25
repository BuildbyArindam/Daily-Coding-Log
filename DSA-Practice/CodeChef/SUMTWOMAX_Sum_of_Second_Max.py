"""
Problem   : Sum of Second Max
Platform  : CodeChef
Link      : https://www.codechef.com/problems/SUMTWOMAX
Difficulty: 1711
Topics    : Fenwick Tree (BIT), Order Statistics, Contribution Technique
Date      : 2026-09-25

Approach:
For each element x (processed in decreasing order of value), x becomes the
"second max" of a subarray [L, R] exactly when there is precisely one element
greater than x inside that subarray. Using a Fenwick Tree over positions,
insert elements from largest to smallest; when processing value x at index i,
query how many larger elements lie to its left/right (already inserted).
Using order-statistics (Fenwick kth-element query) find the nearest and
second-nearest larger elements on each side (l1, l2 to the left; r1, r2 to
the right). The number of subarrays where x is the second max is:
    (l1 - l2) * (r1 - i) + (i - l1) * (r2 - r1)
Multiply by x and accumulate.

Time complexity : O(n log n)  -- n Fenwick insertions + O(log n) kth-queries
Space complexity: O(n)        -- Fenwick tree + position array
"""


# ----------------------------------- Solution --------------------------------------------


import sys

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
    def add(self, idx, value=1):
        while idx <= self.n:
            self.bit[idx] += value
            idx += idx & -idx
    def sum(self, idx):
        result = 0
        while idx > 0:
            result += self.bit[idx]
            idx -= idx & -idx
        return result
    def kth(self, k):
        idx = 0
        bit = self.bit
        step = 1 << (self.n.bit_length() - 1)
        while step:
            nxt = idx + step
            if nxt <= self.n and bit[nxt] < k:
                idx = nxt
                k -= bit[nxt]
            step >>= 1
        return idx + 1

def solve(a):
    n = len(a)
    pos = [0] * (n + 1)
    for i, x in enumerate(a, 1):
        pos[x] = i
    bit = FenwickTree(n)
    answer = 0
    for x in range(n, 0, -1):
        i = pos[x]
        total_greater = bit.sum(n)
        left_greater = bit.sum(i - 1)
        right_greater = total_greater - left_greater
        if left_greater >= 1:
            l1 = bit.kth(left_greater)
        else:
            l1 = 0
        if left_greater >= 2:
            l2 = bit.kth(left_greater - 1)
        else:
            l2 = 0
        if right_greater >= 1:
            r1 = bit.kth(left_greater + 1)
        else:
            r1 = n + 1
        if right_greater >= 2:
            r2 = bit.kth(left_greater + 2)
        else:
            r2 = n + 1
        count = (
            (l1 - l2) * (r1 - i)
            + (i - l1) * (r2 - r1)
        )
        answer += x * count
        bit.add(i)
    return answer

def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(a))

if __name__ == "__main__":
    main()
