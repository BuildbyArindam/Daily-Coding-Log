"""
Problem   : Transformation Cost (TRANCST)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/TRANCST
Difficulty: 1723
Date      : 2026-10-02
Topics    : Bit Manipulation, Binary Search, Precomputation

Approach:
    The target values are 0 and every number whose binary form is a block
    of 1s followed by a block of 0s (at most 30 bits). There are only 466
    such numbers, so they are precomputed once and sorted. For each N, binary
    search finds the smallest target >= N, and the answer is target - N.

Complexity:
    Precompute : O(B^2 log B^2), with B = 30 (about 466 values)
    Per query  : O(log B^2), effectively O(1)
    Space      : O(B^2) for the precomputed list
"""


# ---------------------------------------- Solution -----------------------------------------------


import sys
from bisect import bisect_left
good = [0]
for ones in range(1, 31):
    base = (1 << ones) - 1
    for zeros in range(31 - ones):
        value = base << zeros
        good.append(value)
good.sort()

def solve():
    input = sys.stdin.readline
    T = int(input())
    ans = []
    for _ in range(T):
        N = int(input())
        idx = bisect_left(good, N)
        ans.append(str(good[idx] - N))
    print("\n".join(ans))

if __name__ == "__main__":
    solve()
