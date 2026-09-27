"""
Problem: Dev's Momentum Ledger
Unstop: https://unstop.com/code/practice/661020
Date Solved: 2026-09-28
Difficulty: Medium
Topics: Fenwick Tree (BIT), Coordinate Compression, Binary Search, Sorting, Array, Range Counting

Approach:
For each score x (processed left to right), count how many previously
seen scores fall within [x-k, x+k]. Coordinates are compressed via
sorted(set(scores)) so a Fenwick Tree can be indexed by rank instead of
raw value. bisect_right locates the compressed boundaries for x+k and
x-k-1, and Fenwick prefix sums give count_right and count_left; the
answer for x is their difference. After answering, x itself is inserted
into the Fenwick Tree so future elements can count it.

Time Complexity:  O(n log n) — each element does O(log n) Fenwick ops + O(log n) binary search
Space Complexity: O(n)       — coords array + Fenwick tree array
"""


# ----------------------------------- Solution ----------------------------------------------


import sys
from bisect import bisect_right

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    def add(self, index, value):
        while index <= self.n:
            self.tree[index] += value
            index += index & -index
    def prefix_sum(self, index):
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total

def solve():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))
    coords = sorted(set(scores))
    m = len(coords)
    fenwick = FenwickTree(m)
    answer = []
    for x in scores:
        right = bisect_right(coords, x + k)
        count_right = fenwick.prefix_sum(right)
        left = bisect_right(coords, x - k - 1)
        count_left = fenwick.prefix_sum(left)
        answer.append(count_right - count_left)
        pos = bisect_right(coords, x)
        fenwick.add(pos, 1)
    sys.stdout.write("\n".join(map(str, answer)))

if __name__ == "__main__":
    solve()
