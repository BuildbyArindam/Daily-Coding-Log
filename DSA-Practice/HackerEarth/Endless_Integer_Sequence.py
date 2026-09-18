"""
Problem: Endless Integer Sequence
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/endless-integer-sequence-088184af/
Date Solved: 2026-09-18
Difficulty: Medium
Topics: Algorithms, Binary Search, Binary Indexed Tree (Fenwick Tree)

Approach:
Maintain a Fenwick Tree (BIT) over the sorted set of values that get
deleted, so we can quickly count how many deletions have occurred at
or below any value x. For a "find k-th remaining element" query, binary
search on the answer: for a candidate value `mid`, the count of numbers
<= mid still present in the endless sequence is (mid - deleted_count(mid)).
Find the smallest `mid` where this count >= k.

Time Complexity: O(Q log Q) — each query does an O(log N) BIT update/query
                  wrapped in an O(log(k+N)) binary search.
Space Complexity: O(N) — BIT array + coordinate-compressed deleted values,
                  where N is the number of delete operations.
"""


# -------------------------------- Solution ----------------------------------------------


import sys
from bisect import bisect_right

def solve():
    input = sys.stdin.readline
    Q = int(input())
    queries = []
    all_deleted = []
    for _ in range(Q):
        t, x = map(int, input().split())
        queries.append((t, x))
        if t == 1:
            all_deleted.append(x)
    all_deleted.sort()
    deleted = []
    n = len(all_deleted)
    index = {x: i + 1 for i, x in enumerate(all_deleted)}
    bit = [0] * (n + 1)
    def bit_add(i):
        while i <= n:
            bit[i] += 1
            i += i & -i
    def bit_sum(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s
    def deleted_count(x):
        pos = bisect_right(all_deleted, x)
        return bit_sum(pos)
    answers = []
    for t, x in queries:
        if t == 1:
            bit_add(index[x])
        else:
            k = x
            lo = 1
            hi = k + n
            while lo < hi:
                mid = (lo + hi) // 2
                remaining = mid - deleted_count(mid)
                if remaining >= k:
                    hi = mid
                else:
                    lo = mid + 1
            answers.append(str(lo))
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    solve()
