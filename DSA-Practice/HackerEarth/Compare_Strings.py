"""
Problem   : Compare Strings
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/compare-strings-1-1cb66e03/
Difficulty: Easy
Topics    : Algorithms, Basic programming, Binary search, Searching, String manipulation
Date      : 2026-10-02

Approach:
    Track every index where A and B differ using a Fenwick tree (BIT).
    Each query flips one '0' in B to '1', which updates that index's
    mismatch flag in O(log N). After each query, find the first mismatch
    via a BIT k-th search (k=1) with binary lifting.
    Answer is YES if there is no mismatch (A == B), or if at the first
    mismatch B has '1' and A has '0' (i.e. A <= B). Otherwise NO.

Complexity:
    Time : O((N + Q) log N)  (BIT build is N updates, each query is O(log N))
    Space: O(N)
"""


# ------------------------------------ Solution -----------------------------------------------------------


import sys

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx, value):
        while idx <= self.n:
            self.bit[idx] += value
            idx += idx & -idx

    def sum(self, idx):
        result = 0
        while idx > 0:
            result += self.bit[idx]
            idx -= idx & -idx
        return result

    def find_kth(self, k):
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
    N, Q = map(int, input().split())
    A = input().strip()
    B = bytearray(input().strip())
    fw = FenwickTree(N)
    for i in range(N):
        if A[i] != B[i]:
            fw.add(i + 1, 1)
    out = []
    for _ in range(Q):
        i = int(input())
        idx = i - 1
        if B[idx] == ord('0'):
            B[idx] = ord('1')
            if A[idx] == ord('1'):
                fw.add(i, -1)
            else:
                fw.add(i, 1)
        total_diff = fw.sum(N)
        if total_diff == 0:
            out.append("YES")
        else:
            first = fw.find_kth(1) - 1
            if B[first] == ord('1') and A[first] == ord('0'):
                out.append("YES")
            else:
                out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
