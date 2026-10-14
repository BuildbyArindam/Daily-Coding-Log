"""
Problem   : The Corridor of Vanishing Exhibits
Platform  : Unstop
Link      : https://unstop.com/code/practice/662884
Difficulty: Hard
Topics    : Fenwick Tree, Dynamic Order Statistics, Sorting, Binary Search
Date      : 2026-10-14

Approach:
    Two Fenwick Trees (BITs) over 1..n track which exhibits are still present.
    - Position BIT: 1 at each position that is still present.
        * R x : point-update -1 at position x.
        * N x : count = prefix(x-1) gives the left neighbour via kth(count);
                prefix(x) gives the right neighbour via kth(prefix(x) + 1).
                Return -1 when no neighbour exists.
    - Rank BIT: artifacts are pre-sorted by value (descending), and each
      one's rank is its index in that order. A 1 marks a rank that is still present.
        * R x : also point-update -1 at rank_of_position[x].
        * K x : kth(x) finds the x-th largest remaining artifact by rank.
                Look up its (value, position) in the sorted array.
                Return "-1 -1" if x is out of range.
    kth() uses binary lifting on the BIT, so there is no nested binary search.

Complexity:
    Time : O(n log n + m log n)  (sorting + BIT build + per-query O(log n))
    Space: O(n)
"""


# ---------------------------------------------- Solution --------------------------------------------------------


import sys

input = sys.stdin.readline
n = int(input())
values = list(map(int, input().split()))
m = int(input())
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i
    def query(self, i):
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & -i
        return result
    def kth(self, k):
        idx = 0
        bit = 1 << (self.n.bit_length() - 1)
        while bit:
            nxt = idx + bit
            if nxt <= self.n and self.tree[nxt] < k:
                idx = nxt
                k -= self.tree[nxt]
            bit >>= 1
        return idx + 1
positions = FenwickTree(n)
for i in range(1, n + 1):
    positions.update(i, 1)
sorted_artifacts = sorted(
    [(values[i], i + 1) for i in range(n)],
    reverse=True
)
rank_tree = FenwickTree(n)
rank_of_position = [0] * (n + 1)
for rank, (value, pos) in enumerate(sorted_artifacts, start=1):
    rank_of_position[pos] = rank
    rank_tree.update(rank, 1)
answers = []
for _ in range(m):
    parts = input().split()
    operation = parts[0]
    x = int(parts[1])
    if operation == 'R':
        positions.update(x, -1)
        rank_tree.update(rank_of_position[x], -1)
    elif operation == 'N':
        left_count = positions.query(x - 1)
        if left_count == 0:
            left = -1
        else:
            left = positions.kth(left_count)
        through_x = positions.query(x)
        total = positions.query(n)
        if through_x == total:
            right = -1
        else:
            right = positions.kth(through_x + 1)
        answers.append(f"{left} {right}")
    elif operation == 'K':
        total = rank_tree.query(n)
        if x < 1 or x > total:
            answers.append("-1 -1")
        else:
            rank = rank_tree.kth(x)
            value, pos = sorted_artifacts[rank - 1]
            answers.append(f"{value} {pos}")
print("\n".join(answers))
