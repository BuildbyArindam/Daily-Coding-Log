"""
Problem   : Mystical Numbers (XORGAND)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/XORGAND
Difficulty: 1702
Date      : 2026-09-24
Topics    : Bit Manipulation, Binary Search, Observation

Approach:
    Each query counts indices in [L, R] whose highest set bit differs from
    that of X. Group the 1-based indices of A by bit_length(A[i]) into
    32 sorted lists. For a query, take the list for bit_length(X) and use
    two binary searches to count how many indices fall in [L, R]. Those
    "same" elements are subtracted from the range length (R - L + 1).

Complexity:
    Time : O(N + Q log N) per test case
    Space: O(N)
"""


# ------------------------------------------------ Solution -------------------------------------------------


import sys
from bisect import bisect_left, bisect_right

def solve():
    input = sys.stdin.buffer.readline
    T = int(input())
    out = []
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        pos = [[] for _ in range(32)]
        for i, v in enumerate(A, 1):
            pos[v.bit_length()].append(i)
        Q = int(input())
        for _ in range(Q):
            L, R, X = map(int, input().split())
            k = X.bit_length()
            p = pos[k]
            same = bisect_right(p, R) - bisect_left(p, L)
            out.append(str((R - L + 1) - same))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
