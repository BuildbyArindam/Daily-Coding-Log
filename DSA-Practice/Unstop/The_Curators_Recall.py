"""
Problem: The Curator's Recall
Platform: GeeksforGeeks (via Unstop)
Link: https://unstop.com/code/practice/659241
Difficulty: Hard
Date Solved: 2026-09-04
Topics: Array, Range Queries, Fenwick Tree (BIT), Sorting,
        Coordinate Compression, Offline Queries

Approach:
    Offline query processing with a Fenwick Tree. Sort queries by
    right endpoint r. Sweep current_r from 1 to n; for each new
    element, if the same value was seen before at last_position[val],
    remove that old marker from the BIT (it's no longer the
    "last occurrence" within any prefix ending at/after current_r)
    and add a marker at the new position, then update last_position.
    This keeps the BIT holding exactly one marker per distinct value
    -- the marker at its most recent occurrence up to current_r.
    For each query (l, r), the count of distinct elements in [l, r]
    is prefix_sum(r) - prefix_sum(l-1), since only "last occurrence
    so far" positions are marked as 1.

Time Complexity:  O((n + q) log n)   -- n updates/removals + q queries,
                   each O(log n) on the Fenwick Tree; O(q log q) for
                   the initial sort by r.
Space Complexity: O(n + q)          -- Fenwick Tree array, last_position
                   map, and answers array.
"""


# --------------------------- Solution -----------------------------------


import sys

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx, value):
        while idx <= self.n:
            self.bit[idx] += value
            idx += idx & -idx

    def prefix_sum(self, idx):
        result = 0
        while idx > 0:
            result += self.bit[idx]
            idx -= idx & -idx
        return result

def main():
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    queries = []
    for i in range(q):
        l, r = map(int, input().split())
        queries.append((r, l, i))
    queries.sort()
    fenwick = FenwickTree(n)
    last_position = {}
    answers = [0] * q
    current_r = 0
    for r, l, query_index in queries:
        while current_r < r:
            current_r += 1
            artist = a[current_r - 1]
            if artist in last_position:
                fenwick.add(last_position[artist], -1)
            fenwick.add(current_r, 1)
            last_position[artist] = current_r
        answers[query_index] = (
            fenwick.prefix_sum(r) - fenwick.prefix_sum(l - 1)
        )
    sys.stdout.write("\n".join(map(str, answers)))

if __name__ == "__main__":
    main()
